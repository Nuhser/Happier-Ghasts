scoreboard objectives add happier_ghasts.settings dummy "Happier Ghasts: Settings"

scoreboard players add fix_harnesses happier_ghasts.settings 0
execute if score fix_harnesses happier_ghasts.settings matches 0 run scoreboard players set fix_harnesses happier_ghasts.settings 1