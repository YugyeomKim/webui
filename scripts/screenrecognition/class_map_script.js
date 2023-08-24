const fs = require("fs")
const path = require("path")

const PATH = "../../metadata/screenrecognition/custom_class_map.json"

const highPriorityClasses = {
  statusBar: "STATUS_BAR",
  homeIndicator: "HOME_INDICATOR",
  // TextButton: "TEXT_BUTTON",
  badge: "BADGE",
  keyboard: "KEYBOARD",
}

const classes = {
  text: "TEXT",
  imageRectangle: "IMAGE_RECTANGLE",
  imageEllipse: "IMAGE_ELLIPSE",
  // rectangle: "RECTANGLE",
  // ellipse: "ELLIPSE",
  textField: "TEXT_FIELD",
  // searchField: "SEARCH_FIELD",
  filledButton: "FILLED_BUTTON",
  outlinedButton: "OUTLINED_BUTTON",
  // iconButton: "ICON_BUTTON",
  filledIconButton: "FILLED_ICON_BUTTON",
  outlinedIconButton: "OUTLINED_ICON_BUTTON",
  icon: "ICON",
  segmentedButton: "SEGMENTED_BUTTON",
  switch: "SWITCH",
  topAppBar: "TOP_APP_BAR",
  chip: "CHIP",
  list: "LIST",
  row: "ROW",
  card: "CARD",
  carousel: "CAROUSEL",
  grid: "GRID",
  tabBar: "TAB_BAR",
  tab: "TAB",
  bottomNavigation: "BOTTOM_NAVIGATION",
  backDrop: "BACK_DROP",
  // banner: "BANNER",
  // modal: "MODAL",
  // tooltip: "TOOLTIP",
  radioButton: "RADIO_BUTTON",
  // datePicker: "DATE_PICKER",
  // timePicker: "TIME_PICKER",
  // quantityPicker: "QUANTITY_PICKER",
  // bottomAppBar: "BOTTOM_APP_BAR",
  other: "OTHER",
}

const classMapMerged = { ...highPriorityClasses, ...classes }

const classMap = {
  "idx2Label": {
    "0": "BACKGROUND",
    "1": "OTHER"
  },
  "label2Idx": {
    "BACKGROUND": 0,
    "OTHER": 1
  }
}

let i = 2
for (const value of Object.values(classMapMerged)) {
  if (value === "OTHER") continue
  
  classMap["idx2Label"][i.toString()] = value
  classMap["label2Idx"][value] = i
  i++
}

const classMapString = JSON.stringify(classMap)

fs.writeFileSync(path.join(__dirname, PATH), classMapString)