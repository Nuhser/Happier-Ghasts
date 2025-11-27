execute as @e[type=item_display, tag=custom_crafter] at @s \
    unless predicate custom_crafter:custom_crafter_present \
    run kill @s

# TODO: Create loot table that drops all items from inside the dropper as well as the custom crafter spawn item