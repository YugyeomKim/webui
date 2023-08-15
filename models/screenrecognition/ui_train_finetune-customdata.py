if __name__ == "__main__":

    CHECK_INTERVAL_STEPS = 4000

    ARTIFACT_DIR = "./checkpoints_screenrecognition_web350k-vins-customdata"

    import os

    if not os.path.exists(ARTIFACT_DIR):
        os.makedirs(ARTIFACT_DIR)

    from ui_datasets import *
    from ui_models import *
    from pytorch_lightning import Trainer
    from pytorch_lightning.callbacks import *
    import torch
    import datetime
    from pytorch_lightning.loggers import TensorBoardLogger
    import json
    
    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning) # FutureWarning 제거

    CLASS_MAP_FILE = "../../metadata/screenrecognition/custom_class_map.json"
    with open(CLASS_MAP_FILE, "r") as f:
        class_map = json.load(f)
    FINETUNE_CLASSES = len(class_map["idx2Label"])
    print("FINETUNE_CLASSES: " + str(FINETUNE_CLASSES))

    logger = TensorBoardLogger(ARTIFACT_DIR)
    
    data = CustomDataModule()

    model = UIElementDetector.load_from_checkpoint('../../downloads/checkpoints/screenrecognition-web350k-vins.ckpt', val_weights=None, lr=0.01)
    model.hparams.num_classes = FINETUNE_CLASSES

    mod = model.model.head.classification_head
    model.model.head.classification_head.cls_logits = torch.nn.Conv2d(mod.cls_logits.in_channels, mod.num_anchors * FINETUNE_CLASSES, kernel_size=3, stride=1, padding=1)
    model.model.head.classification_head.num_classes = FINETUNE_CLASSES
    model.hparams.num_classes = FINETUNE_CLASSES
    
    print("***********************************")
    print("checkpoints: " + str(os.listdir(ARTIFACT_DIR)))
    print("***********************************")
    
    
    checkpoint_callback = ModelCheckpoint(dirpath=ARTIFACT_DIR, every_n_train_steps=CHECK_INTERVAL_STEPS, save_last=True)
    checkpoint_callback2 = ModelCheckpoint(dirpath=ARTIFACT_DIR, filename= "screenrecognition",monitor='mAP', mode="max", save_top_k=1)
    
    earlystopping_callback = EarlyStopping(monitor="mAP", mode="max", patience=10)

    trainer = Trainer(
        # gpus=1,
        accelerator="gpu",
        devices='auto',
        gradient_clip_val=1.0,
        accumulate_grad_batches=2,
        callbacks=[checkpoint_callback, checkpoint_callback2, earlystopping_callback],
        min_epochs=10,
        max_epochs=-1,
        logger=logger
    )
    
    if os.path.exists(os.path.join(ARTIFACT_DIR, "last.ckpt")):
        model = UIElementDetector.load_from_checkpoint(os.path.join(ARTIFACT_DIR, "last.ckpt"))

    trainer.fit(model, data)
