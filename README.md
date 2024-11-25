# whiteout survival database

all the content in this repo so far has been obtained by me through in game screenshots or manual data entry

current contents:
1. [chief gear images](https://github.com/zenpaiang/wos-database/tree/master/chief_gear) (only has up to mythic t2 3-star)
2. [chief gear costs](https://github.com/zenpaiang/wos-database/blob/master/chief_gear.json)

# obtaining of chief gear images

i used this as an opportunity to learn how to do image recognition with machine learning. using the `ultralytics` python module, i trained a `yolo11n` model to recognize chief gear from a set of screenshots (get the model [here](https://github.com/zenpaiang/wos-database/blob/master/chief_gear.pt) and the example code [here](https://github.com/zenpaiang/wos-database/blob/master/chief_gear.py))

then, i used the trained model to recognize chief gear in a folder of 156 screenshots of chief gear to extract cropped images of each piece.