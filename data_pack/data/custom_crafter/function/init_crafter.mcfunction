# set the custom crafter dropper block and remove init-tag
execute at @e[type=item_display, tag=custom_crafter, tag=init] \
    run setblock ~ ~ ~ dropper[facing=up]{\
        CustomName: {\
            translate: "item.customCrafter.customCrafter.name",\
            fallback: "Advanced Crafting Table"\
        },\
        LootTable: "custom_crafter:blocks/custom_crafter",\
        components: {\
            "minecraft:custom_data": {"custom_crafter": true},\
            "minecraft:enchantment_glint_override": true\
        }\
    }

tag @e[type=item_display, tag=custom_crafter, tag=init] remove init