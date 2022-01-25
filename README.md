## STAW: Solitaire
A variant gameplay implementation of <b>Star Trek Attack Wing (STAW)</b> <u>inspired from</u> <b>Leo Zappa's Simple Solitaire Rules version 2.0</b>.

Source Material: https://boardgamegeek.com/thread/1221629/leos-simple-solitaire-rules-playtest-and-developme

### What does it do?
It allows the multi-player table top game to be played as solo.

<b>NOTE:</b> The official table-top rules are applied with the following exceptions:
* No <b>Planning Phase</b>
* The <b>Captain Skill Level</b> is ignored which will nullifies certain cards' action and/or ability
* The <b>Faction</b> hierarchy is ignored

<b>NOTE:</b> The solitaire rules version 2.0 are applied with the following exceptions:
* User will provide the number of ships deployed in the <b>Play Area</b>
* User will provide individual ship name instead of using physical Captain Tokens
* A data structure to mimic the physical opaque container that stores the Captain Tokens
* Implement a variant chit-pull mechanism (i.e. chit = Captain Token) by generating a list of ships per gameplay phase

### How does it work?
A <u>physical copy</u> of the <b>Star Trek Attack Wing Starter Set</b> is <u>required</u>; better if purchased expansion packs are available.

A computer hosted on Linux, Mac OS or Windows with a copy of the <b>Python 3 interpreter</b> (https://www.python.org/) installed.

The program is executed on the command-line | terminal using the command:<br>
<b>python3 solitaire.py</b>

The program will perform the following:
* Asks the user once on the number of ships deployed
* Asks the user once for the Ship Names
* Generate a list of ship names for the <b>Activation Phase</b> that determines ship movement in succession
* Generate a list of ship names for the <b>Combat Phase</b> that determines ship attack in succession
* Generate a reminder of the clean-up rules for the <b>End Phase</b>

The gameplay (not the program) will conclude when the following conditions are met:
* Survival of the fittest = one (1) ship left in the <b>Play Area</b>
* Gameplay narration (user discretion)
* Termination of the program (user discretion)
