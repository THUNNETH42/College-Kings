default persistent.name = ""
default scopeDict = {}

init python:
    sceneGalleryItems = []

    class SceneGallery:
        def __init__(self, label, scope=None):
            self.label = label
            self.idleImg = "sceneGallery/images/gallery{}.webp".format(len(sceneGalleryItems) + 1)
            self.hoverImg = "sceneGallery/images/gallery{}_hover.webp".format(len(sceneGalleryItems) + 1)

            if scope is None: self.scope = {}
            else: self.scope = scope

            sceneGalleryItems.append(self)

    def updateScope(newScope):
        rv = scopeDict.copy()
        rv.update(newScope)
        return rv

    ## SCENE GALLERY ITEMS HERE
        # v1
    SceneGallery("sexdream1") #Riley
        # v2
    SceneGallery("v1_tomShoutBack") #Tom
        # v3
    SceneGallery("continuem") #Aubrey, day 4, aubreysex
        # v5
    SceneGallery("fkcon") #Adam
        # v6
    SceneGallery("emsex_a") #Emily, day 7, v6_emilysex
    SceneGallery("aubreysexb") #Aubrey, day 7, aubreysex2
        # v7
    SceneGallery("rileysexscene") #Riley, day 10, v7_rileysex
    SceneGallery("brbj") #Aubrey, day 11, bathroomblowjob
        # v8
    SceneGallery("v8_cl_start") #2, Chloe, day 11, v8_chloesex
    SceneGallery("v8_ri_start") #3, Riley, day 11, v8_riley_lewd_ending
    SceneGallery("hoco_amb_night") #5, Amber, day 11, v8_hocoamber
    SceneGallery("int_deal_w_josh") #28, Lars Joe
    SceneGallery("amber_sex_at_joshs") #30, Amber, day 14, amberSexAtJoshs
        # v9
    SceneGallery("v9_aubrey_scene_lake") #7, Aubrey, day 16, v9_aubrey_lake
    SceneGallery("v9_emily_dorm") #16, Emily, day 17, v9_em_dorm_scene
    SceneGallery("v9_ri_sex") #34, Riley, day 19, v9_sex_with_riley
    SceneGallery("v9_make_out_w_lin") #39, Lindsey, day 19, lindseyfirstkiss
        # v10
    SceneGallery("v10_mc_vs_ryan_fight") #6, Ryan
    SceneGallery("v10_mc_vs_imre_fight") #7, Imre
    SceneGallery("v10s17_galleryScene") #17, Aubrey, day 20, aubrey_bathroom_sex
    SceneGallery("v10_lauren_room_sg", scope={"laurenrs": True}) #24, Lauren, day 21, v10_lauren_suck (otherwise forced)
    SceneGallery("v10_amber_skatepark_sg") #26, Amber, day 21, v10_ambersex
    SceneGallery("v10s30_galleryScene") #30, Chloe, day 22, v10_chloe_locker
    SceneGallery("v10s40_galleryScene", scope={"rileyrs": True}) #40, Riley, day 23, v10_ri_sex
        # v11
    SceneGallery("v11s5_galleryScene") #5, Candy, day 24, v11_fucked_candy
    SceneGallery("v11_aubrey_plane_sex_sg") #13, Aubrey, day 26, v11_aubrey_sex
    SceneGallery("v11_ms_rose_sex_sg") #28, Rose, day 27, v11_msrose_scene
    SceneGallery("v11s28a_galleryScene") #28a, Samantha, day 27, v11_samantha_spa
    SceneGallery("v11_riley_sex_sg") #35, Riley, day 28, v11_rileysex
    SceneGallery("v11_chloe_sex_scene") #41b, Chloe, day 29, v11_chloe_sex
        #v12
    SceneGallery("v12_lindsey_sex") #17, Lindsey, day 32, v12_lindsey_sex
    SceneGallery("v12_ms_rose_sex_sg") #23, Rose, day 33, v12_msrose_sex
    SceneGallery("v12_lauren_sex_sg") #29, Lauren, day 34, v12_lauren_sex
    SceneGallery("v12_nora_sex") #35a, Nora, day 35, v12_nora_sex
        #v13
    SceneGallery("v13s16a") #16a, Riley, day 37, v13_rileysex
    SceneGallery("v13s25_emmysg") #26, Emmy, day 38, v13_emmysex
    SceneGallery("v13s40_sg") #40, Chloe, day 39, v13_chloe_sex
    SceneGallery("v13s50a") #50a, Emily, day 40, v13_emilysex
        #v14
    SceneGallery("") #3d
    SceneGallery("") #21a
    SceneGallery("") #25a
    SceneGallery("") #36
    SceneGallery("") #53a

screen spoiler():
    modal True

    add "images/darker.webp"

    use endfrTemplate:
        text "Warning: The scene gallery contains spoilers for the story of the game. Are you sure you want to continue?":
            style "endfree"
            xalign 0.5

        hbox:
            align (0.5, 1.0)
            spacing 200

            textbutton "Yes":
                action [Hide("spoiler"), ui.callsinnewcontext("sceneGalleryNameChange"), Show("sceneGallery")]

            textbutton "No":
                action Hide("spoiler")


screen sceneGallery():
    tag menu
    modal True

    add "sceneGallery/images/sceneGalleryBackground.webp"

    vpgrid:
        cols 4
        spacing 40
        pos (78, 200)
        ysize 700
        scrollbars "vertical"
        draggable True
        mousewheel True

        for sceneGalleryItem in sceneGalleryItems:
            imagebutton:
                action Replay(sceneGalleryItem.label, scope=updateScope(sceneGalleryItem.scope))
                idle Transform(sceneGalleryItem.idleImg, size=(400, 226))
                hover Transform(sceneGalleryItem.hoverImg, size=(400, 226))
                insensitive Transform(im.Blur(sceneGalleryItem.idleImg, 3), size=(400, 226))

    imagebutton:
        idle "images/backtransp.webp"
        hover "images/back.webp"
        pos (79, 933)
        action Show("main_menu")

label sceneGalleryNameChange:
    
    scene black
    if not persistent.name.strip():
        $ persistent.name = renpy.input(_("What's your name?"), default=_("Alex")).strip() or _("Alex")

    $ scopeDict = {"name":persistent.name}

    return