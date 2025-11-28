# make item entities enchantable
execute as @e[type=minecraft:item,nbt=!{Item: {components: {"minecraft:enchantable": {value: 15}}}}] run data merge entity @s {Item: {components: {"minecraft:enchantable": {value: 15}}}}

# make item in player's cursor enchantable
execute as @a if items entity @s player.cursor #minecraft:harnesses[!enchantable={value:15}] run item modify entity @s player.cursor happier_ghasts:make_harness_enchantable

# make item in Happy Ghast's inventory enchantable
execute as @e[type=minecraft:happy_ghast] if items entity @s armor.body #minecraft:harnesses[!enchantable={value:15}] run item modify entity @s armor.body happier_ghasts:make_harness_enchantable