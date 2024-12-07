# whiteout survival database

all the content in this repo so far has been obtained by me through in game screenshots or manual data entry

current contents:
1. [chief gear images](https://github.com/zenpaiang/wos-database/tree/master/chief_gear) (only has up to mythic t2 3-star)
2. [chief gear costs](https://github.com/zenpaiang/wos-database/blob/master/chief_gear.json) (only has up to mythic t2 3-star)
3. [chief charm images](https://github.com/zenpaiang/wos-database/tree/master/chief_charm)
4. [chief charm costs](https://github.com/zenpaiang/wos-database/blob/master/chief_charm.json)

# chief gear images and costs

chief gear images are organized by rarity into folders with an `identifier`. for example:  
- Mythic T2 3-Star: `mythic_t2_3`
- Epic T1: `epic_t1_0`
- Rare: `rare_0`

in `chief_gear.json`, each key is an `identifier` for a rarity of chief gear. the data stored with that key contains the proper name of the rarity, and how much `hardened_alloy`, `polishing_solution`, `design_plans`, and `amber` (only for >legendary gear, which is not included in this database for now) is needed to upgrade to that rarity.

it also contains the power and stat bonuses for each rarity of chief gear.

# chief charm images and costs

chief charm images are organized by their type, e.g. `keenness` (lancer stat charm), `protection` (infantry stat charm), or `vision` (marksman stat charm)

they are sorted into folders and are named by their level.

each key in `chief_charm.json` are the level of the charm. they contain the cost of the charm in `charm_design`(s) and `charm_guide`(s), their stat percentages, and the amount of power they give you.

# stories

## obtaining of chief gear images

i used this as an opportunity to learn how to do image recognition with machine learning. using the `ultralytics` python module, i trained a `yolo11n` model to recognize chief gear from a set of screenshots (get the model [here](https://github.com/zenpaiang/wos-database/blob/master/chief_gear.pt) and the example code [here](https://github.com/zenpaiang/wos-database/blob/master/chief_gear.py))

then, i used the trained model to recognize chief gear in a folder of 156 screenshots of chief gear to extract cropped images of each piece.

## obtaining of chief charm images

this one does not have as fun of a story as the obtaining of chief gear images. i just took screenshots of every charm and wrote a python script to remove the backgrounds, and trim it, replacing it with 