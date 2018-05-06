# fusion-tools
This is a collection of code, tools, and information to support running a "West Marches" 5e D&D campaign using modern tools and spiced to my tastes.

## setup
- Have Python 3.3.* as default version on OS (`python`)
- At base of repository run: 
    + `python -m venv venv`
    + Activate your venv: `. ./venv/bin/activate` or `venv\Scripts\activate.bat`
    + `pip install --upgrade pip`
    + `pip install -r requirements.txt`
<!-- - Use the following shebang: `#!/usr/bin/env python` -->
- Before running any script, activate your venv: `./venv/bin/activate`
- Before releasing, use pip freeze > requirements.txt
    + remove `pkg-resources` line from requirements.txt
- To run tests: `python -m unittest discover`
- To run tests with coverage: `coverage run -m unittest discover`
- To generate coverage report: `coverage html --omit="*/venv*"`
- View report by opening: `./htmlcov/index.html`
- You'll need to provide credentials for each piece of the flow to work
    + Oauth tokens will be used for most authetication
- These credentials should be stored in *.cred files in the `credentials` directory
- At work, you'll need to `set http_proxy=http://...` and `set https_proxy=http://...` to punch through that proxy
- Also, in a Windows terminal, you may encounter issues when echoing unicode characters for debug purposes, so execute the following: `chcp 65001`

Now all scripts should reference the version of python in that venv, install all additional libs from that path

## attribution
- 

## docs
- http://praw.readthedocs.io/en/latest/index.html
- 

# Helpful Link Index
- https://www.dndbeyond.com/ [official online references/tools]
## DM Tools
- http://homebrewery.naturalcrit.com/ [homebrew formatting]
- http://www.naturalcrit.com/ [achievement badges]
- https://www.reddit.com/r/DnDBehindTheScreen/
- https://www.adventurelookup.com/adventures/
- http://bankuei.wordpress.com/2010/03/27/the-same-page-tool/
- https://www.acaeum.com/ddindexes/modcode.html
- http://grognardia.blogspot.com/2008/09/30-greatest-d-adventures-of-all-time.html
### Historical Reference
- http://www222.pair.com/sjohn/fief.htm
- http://www222.pair.com/sjohn/blueroom/demog.htm
- http://www.grey-company.org/Circle/language/com2elv.htm
### Audio
- http://www.ambient-mixer.com/
- http://www.tabletopaudio.com/#
- https://incompetech.com/music/royalty-free/music.html
### Random Generators
- http://www.apolitical.info/webgame/tables
- http://donjon.bin.sh/
- https://www.reddit.com/r/BehindTheTables/wiki/index
- http://www.lordbyng.net/inspiration/tables.php
- http://roll1d12.blogspot.com/
- http://inkwellideas.com/free-tools/rumor-generator/
- https://www.reddit.com/r/DnD/comments/2sjvgy/what_kind_of_random_roll_tables_are_out_there/
- https://www.reddit.com/r/DnD/comments/36ngej/donjon_is_one_of_the_best_dm_resources_ive_ever/
- http://fantasynamegenerators.com/
- http://redkatart.com/treasure5e/treasureGen.php
- https://www.aidedd.org/adj/idees-aventures/
- http://www.wizards.com/dnd/hook/Welcome.asp#
- http://dndhook.madbs.in/
- http://anydice.com/
- http://inkwellideas.com/free-tools
### Monster Reference
- http://surfarcher.blogspot.com/2014/07/d-5e-monsters-master-index.html
- http://chisaipete.github.io/bestiary/
### Magic Items
- http://donjon.bin.sh/5e/magic_items/
- http://www.tribality.com/2015/11/02/dd-5e-magic-item-guide/
- https://drive.google.com/file/d/0B8XAiXpOfz9cMWt1RTBicmpmUDg/view
- http://www.lordbyng.net/inspiration/tables.php
### Encounter Building & Tracking
- http://kobold.club/fight/#/encounter-builder
- http://tools.goblinist.com/5enc
- http://dhmholley.co.uk/encounter-calculator-5th/
- http://www.improved-initiative.com/e/9kbtj6ee
### Map Building
- https://inkarnate.com/maps#/new
- http://www.yeoldemapmaker.com/editor/
- http://deepnight.net/tools/tabletop-rpg-map-editor/
- http://www.hexographer.com/
- http://www.dungeonographer.com/
- http://cityographer.com/
### Conversion Guides & References
- http://www.tribality.com/2015/09/28/old-school-dd-dungeon-module-conversion-guide/
- https://docs.google.com/document/d/1gwlJEh8hI63FzppPtbjpOeaxhbNuDENvWl4uowgq9RM/mobilebasic
## PC Tools
- http://dicecloud.com/
- http://www.digitaldungeonmaster.com/dd-5e-character-sheets.html
- http://dungeonsmaster.com/pre-generated-character-library-dndnext/
- http://dnd.wizards.com/articles/features/character_sheets
- http://chicken-dinner.com/5e/5e-point-buy.html#triton&NA&14&10&15&10&8&14&0&0&27&15&8&19&15&12&9&7&5&4&3&2&1&0&1&2&4&6&9
### Spell References
- http://thebombzen.github.io/grimoire/
- http://dndbits.com/spells.php
- https://donjon.bin.sh/5e/spells/
### Rule References
- http://5thsrd.org/
- http://dndbits.com/index.php
- https://crobi.github.io/dnd5e-quickref/preview/quickref.html
