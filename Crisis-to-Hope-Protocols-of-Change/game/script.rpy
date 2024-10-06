
define l = Character("Lucas Alvarez (Politician)", color="#ffcc00")
define a = Character("Amara Singh (Activist)", color="#ff6666")
define e = Character("Dr. Elena Greene (Environmental Scientist)", color="#66ccff")
define y = Character("Yusuf Patel (Engineer)", color="#66ff66")
default player = Character("", color="#0003dc")
default main = ""

default score = 0
# Backgrounds
image bg_summit = "images/bg_summit.png"
image bg_water = "images/bg_water.png"
image bg_ecosystem = "images/bg_ecosystem.png"
image bg_emergency = "images/bg_emergency.png"
image avatar_adam = "images/avatar1.png"  # Adam's avatar
image avatar_eve = "images/avatar2.png"   # Eve's avatar
image char_cover = "images/char-cover.png"
image Elena = "images/elena.png"
image Yusuf = "images/Yusuf.png"
image lucas = "images/lucas.png"
image Amara = "images/Amara.png"
image player_image = "images/[main].png" 
image bg_bio = "images/bg_bio.png"
image bg_pedo = "images/bg_pedo.png"
image bg_matrix = "images/matrix.png"
# Music
define bgm_dramatic = "audio/bgm_dramatic.ogg"
define bgm_tense = "audio/bgm_tense.ogg"
define bgm_hopeful = "audio/bgm_hopeful.ogg"

# Initialize the selected_avatar variable
default selected_avatar = None

label start:
    scene char_cover
    player "GOAL: Players aim is to understand the interconnectedness of environmental systems and how their decisions impact climate change. They are encouraged to make responsible choices that promote climate justice and global responsibility."
    player "Choose an avatar."
    # Show the avatars in a side-by-side layout
    show avatar_adam at Position(xalign=0.25, yalign=0.9) with dissolve
    show avatar_eve at Position(xalign=0.75, yalign=0.9) with dissolve

    # Display buttons for avatar selection under each image
    menu:
            "Liam Donovan" if not selected_avatar:
                label Adam:
                    hide avatar_adam
                    hide avatar_eve
                    $ selected_avatar = "Liam"
                    show avatar_adam at Position(xalign=0.25, yalign=0.5) with dissolve 
                    player "You have selected Liam Donovan."
                    $ player = Character("Liam", color="#00bbdc")
                    $ main = "avatar1"
                    jump introduction
            "Eve Carter" if not selected_avatar:
                label Eve:
                    $ selected_avatar = "Eve"
                    $ main = "avatar2"
                    hide avatar_adam
                    hide avatar_eve
    # Adjust width and height using size
                    player "You have selected Eve Carter."
                    $ player = Character("Eve", color="#00bbdc")
                    jump introduction
label introduction:
    scene bg_summit
    show lucas at left with dissolve
    l "Welcome, everyone. As we gather here today, the reports are clear: the situation is dire. Climate change is accelerating, and we must act swiftly."
    l "However, we need to consider our options carefully. We push too hard, and economies could collapse. We don’t push hard enough, and our future goes up in smoke. The question is: where’s the balance?"
    hide lucas
    show Amara at left with dissolve
    a "Balance? We’re long past the point of balance, Lucas. Climate justice isn’t about protecting the interests of big polluters. People are dying—droughts, floods, famine! We don’t have time for compromise."
    hide Amara
    show Elena at left  with dissolve 
    e "The data doesn’t lie. Every year we delay, emissions rise, and the 2°C target becomes harder to achieve. We need to implement serious reductions now, or we’re looking at 3°C or more by the end of the century."
    hide Elena
    show Yusuf at left  with dissolve 
    y "But technology can solve this, right? We don’t have to pull the emergency brake and crash the economy. We could invest in clean tech, use carbon capture, transition gradually. Isn’t that more realistic?"
    hide Yusuf
    menu:
        "Commit to Aggressive Emissions Targets":
            $ choice = "aggressive"
            show player_image at left
            player "Let’s commit to reducing emissions by 50%% by 2030, no exceptions. We need to send a strong message."
            hide player_image 
            show lucas at left with dissolve
            l "That’s a bold move! It will show our commitment, but we need to prepare for backlash from some member countries."
            hide lucas
            show Elena at left  with dissolve 
            e "This could inspire others to follow suit. If we stand united, we can create a global movement."
            hide Elena
            show Amara at left with dissolve
            a "It’s time to be bold. People need to see real change!"
            hide Amara
            $ score +=10
            jump outcome_aggressive

        "Implement Carbon Trading":
            $ choice = "carbon_trading"
            show player_image at left
            player "We’ll set up a carbon trading system to allow flexibility in emissions cuts. This way, industries can adjust more easily."
            hide player_image
            show lucas at left with dissolve
            l "A more flexible approach could encourage countries to participate, but we need to ensure it doesn’t become a loophole for big polluters."
            hide lucas
            show Elena at left  with dissolve
            e "We must set strict guidelines to prevent exploitation of this system. If we do it right, it can be a valuable tool."
            hide Elena
            $ score +=5
            jump outcome_carbon_trading

        "Compromise on Economic Growth":
            $ choice = "compromise"
            show player_image at left
            player "Let’s allow slower emissions cuts to maintain economic stability in vulnerable regions."
            hide player_image
            show lucas at left with dissolve
            l "This could help us avoid immediate backlash, but it might not be enough to meet our long-term goals."
            hide lucas
            show Elena at left  with dissolve
            e "This will send the wrong message. Compromising now may cost us dearly in the future."
            hide Elena
            $ score +=1
            jump outcome_compromise
label outcome_aggressive:
    show Elena at left  with dissolve
    e "The agreement sets strict targets, and nations unite to work on reducing emissions. Initial backlash from industry groups occurs, but public support grows as the data is shared."
    hide Elena
    show Amara at left with dissolve
    a "The world starts to stabilize, leading to further collaborative efforts."
    hide Amara
    stop music fadeout 1.0
    jump hydrosphere_protocols

label outcome_carbon_trading:
    show Elena at left  with dissolve
    e "The carbon trading system provides some emissions reductions, but industries exploit loopholes."
    hide Elena
    show Amara at left with dissolve
    a "Future missions will involve dealing with the consequences of insufficient action."
    hide Amara
    stop music fadeout 1.0
    jump hydrosphere_protocols

label outcome_compromise:
    show Elena at left  with dissolve
    e "Emissions continue to rise, and the player faces a future mission with communities suffering from increased climate impacts."
    hide Elena
    show Amara at left with dissolve
    a "This leads to social unrest and demands for immediate action."
    hide Amara
    stop music fadeout 1.0
    jump hydrosphere_protocols

label hydrosphere_protocols:
    
    scene bg_water
    show Yusuf at left  with dissolve 
    y "We’ve developed several innovative techniques to conserve water and improve water quality."
    y "But the real challenge isn’t the technology; it’s getting industries and governments to adopt these solutions."
    hide Yusuf
    show Amara at left with dissolve
    a "And why aren’t they adopting them? Is it because it costs too much? Or because they don’t want to change their profit-driven models? We need to hold these corporations accountable."
    hide Amara

    menu:
        "Launch a Global Water Conservation Fund":
            show player_image at left
            player "We’ll create a global fund to subsidize water conservation techniques in developing nations."
            hide player_image
            $ score +=10
            jump outcome_water_good

        "Focus on Awareness Campaigns":
            show player_image at left 
            player "We’ll invest in awareness campaigns about the importance of water conservation before implementing regulations."
            hide player_image
            $ score +=5
            jump outcome_water_moderate

        "Delay Action for Economic Stability":
            show player_image at left 
            player "Let’s postpone any significant changes for ten years to give industries time to adapt."
            hide player_image
            $ score +=1
            jump outcome_water_bad

label outcome_water_good:
    show Elena at left  with dissolve
    e "The Global Water Conservation Fund successfully drives innovation and adoption of sustainable practices. Water security improves in vulnerable regions."
    hide Elena
    show Amara at left with dissolve
    a "This approach gains international support, leading to long-term positive effects."
    hide Amara
    jump biosphere_protocols

label outcome_water_moderate:
    show Elena at left  with dissolve
    e "Awareness campaigns raise public consciousness, but without significant policy changes, water security remains a challenge."
    hide Elena
    show Amara at left with dissolve
    a "While it's a step in the right direction, the delay in aggressive action may come with future costs."
    hide Amara
    jump biosphere_protocols

label outcome_water_bad:
    show Elena at left  with dissolve
    e "By delaying action for economic stability, we avoided immediate disruptions. However, as water scarcity worsens, the impacts become increasingly severe."
    hide Elena
    show Amara at left with dissolve
    a "Communities are suffering, and the delayed response has cost us precious time. It's a grim outlook moving forward."
    hide Amara
    jump biosphere_protocols


label biosphere_protocols:
    
    scene bg_bio
    show Elena at left  with dissolve
    e "We’ve seen alarming rates of biodiversity loss. Our ecosystems are collapsing, and we must act to protect them. If we don’t, the impacts will be catastrophic."
    hide Elena
    show Amara at left with dissolve
    a "The health of our planet is tied to the health of its ecosystems. We need to preserve biodiversity while addressing climate change."
    hide Amara
    show Yusuf at left  with dissolve 
    y "We have the technology to restore habitats and improve ecosystem resilience. We just need the political will to implement it."
    hide Yusuf
    menu:
        "Commit to a Global Biodiversity Fund":
            show player_image at left with dissolve
            player "We’ll establish a global fund dedicated to restoring and preserving ecosystems worldwide"
            hide player_image
            $ score +=10
            jump outcome_bio_good

        "Implement Conservation Programs":
            show player_image at left with dissolve
            player "We’ll initiate conservation programs but will rely heavily on volunteer efforts and local organizations."
            hide player_image
            $ score +=5
            jump outcome_bio_moderate

        "Allow Development in Sensitive Areas":
            show player_image at left with dissolve
            player "Let’s prioritize economic development over conservation in critical habitats."
            hide player_image
            $ score +=1
            jump outcome_bio_bad

label outcome_bio_good:
        show lucas at left with dissolve
        l "This could be the key to restoring balance. If we can invest in natural solutions, it will benefit both the planet and our economy."
        hide lucas
        show Elena at left  with dissolve
        e "This will require collaboration across nations, but the potential for positive impact is enormous."
        hide Elena
        jump pedosphere_protocols

label outcome_bio_moderate:
    show Yusuf at left  with dissolve 
    y "This can raise awareness and get communities involved, but it may lack the necessary resources for significant impact."
    hide Yusuf
    show Amara at left with dissolve
    a "Community involvement is crucial, but we need strong support from governments and NGOs to make real changes."
    hide Amara
    jump pedosphere_protocols

label outcome_bio_bad:
    show lucas at left with dissolve
    l "This could boost the economy, but we risk losing vital ecosystems and biodiversity."
    hide lucas
    show Elena at left  with dissolve
    e "You’re choosing short-term gains over long-term survival. This will harm not just the environment but human well-being."
    hide Elena
    jump pedosphere_protocols

label pedosphere_protocols:
    scene bg_pedo   
    show Elena at left  with dissolve
    e "Healthy soil is essential for food security, water filtration, and carbon storage. We must implement measures to protect and restore soil health."
    hide Elena
    show Amara at left with dissolve
    a "Soil degradation is often overlooked, but it’s crucial for our survival. We need to prioritize sustainable agricultural practices"
    hide Amara
    show Yusuf at left  with dissolve 
    y "We can use technology to improve soil health and enhance agricultural productivity. It’s a win for farmers and the environment."
    hide Yusuf
    show lucas at left with dissolve
    l "We need a comprehensive approach that integrates soil health with our other climate initiatives."
    hide lucas
    menu:
        " Establish a Global Soil Health Initiative":
            show player_image at left
            player "We’ll create a global initiative to promote sustainable agricultural practices and soil restoration"
            hide player_image 
            $ score +=10
            jump outcome_pedo_good

        "Promote Local Soil Conservation Programs":
            show player_image at left 
            player "We’ll promote local soil conservation programs but rely on community volunteers to implement them"
            hide player_image
            $ score +=5
            jump outcome_pedo_moderate

        "Allow Intensive Agriculture in Vulnerable Areas":
            show player_image at left
            player "Let’s prioritize intensive agricultural practices to boost production, even in sensitive soil areas."
            hide player_image
            $ score +=1
            jump outcome_pedo_bad

label outcome_pedo_good:
        show Yusuf at left  with dissolve 
        y "This initiative could revolutionize agriculture and combat soil degradation on a large scale"
        hide Yusuf
        show Amara at left with dissolve
        a "Finally, a focus on the foundation of our food systems. This is crucial for climate resilience."
        hide Amara
        jump final_stand

label outcome_pedo_moderate:
    show Elena at left  with dissolve
    e "Community involvement is great, but we need structured support to ensure these programs are effective."
    hide Elena
    show lucas at left with dissolve
    l "Local programs can make a difference, but without funding, their impact may be limited"
    hide lucas
    jump final_stand

label outcome_pedo_bad:
    show Amara at left with dissolve
    a "This could lead to soil erosion and degradation. You’re prioritizing short-term gains over long-term sustainability."
    hide Amara
    show Elena at left  with dissolve
    e "This will have severe consequences for food security and our environment. We cannot afford to ignore soil health"
    hide Elena
    jump final_stand
label final_stand:
    scene bg_emergency
    show lucas at left with dissolve
    l "We’ve hit the tipping point. Heatwaves are becoming deadly, food supplies are dwindling, and entire nations are at risk of disappearing under rising seas."
    l "We have one last chance to get this right."
    hide lucas
    show Elena at left  with dissolve
    e "Our models show we can still stabilize the climate if we reach net-zero by 2050, but every year we delay, the window narrows. We need immediate, unprecedented action."
    hide Elena
    show Amara at left with dissolve
    a "The people are ready to act. We’ve seen the protests, the grassroots movements. They’re demanding change now. But are we ready to give them what they need?"
    hide Amara
    menu:
        "Implement an Emergency Global Climate Fund":
            $ final_choice = "fund"
            show player_image at left with dissolve
            player "We’ll establish an emergency global climate fund to address both mitigation and adaptation on an unprecedented scale. Every nation must contribute, and every vulnerable region must benefit."
            player "This could work, but we’ll need every major economy on board. If even one country pulls out, the whole plan could fall apart."
            hide player_image
            show Elena at left  with dissolve
            e "It’s risky, but it’s the best option we have. We can’t afford to go slow anymore."
            hide Elena
            $ score +=10
            jump end

        "Call for Immediate National Emergency Actions ":
            $ final_choice = "emergency_actions"
            show player_image at left with dissolve
            player "Let’s call for immediate national emergency actions to address current crises, but without a formal funding structure yet."
            hide player_image
            show Elena at left  with dissolve
            e "Immediate actions are necessary, but without funding, the impact will be limited. How do we ensure sustainability?"
            hide Elena
            $ score +=5
            jump end

        "Delay Action for Political Stability":
            $ final_choice = "delay"
            show player_image at left with dissolve
            player "Let’s postpone radical changes for a few years to maintain political stability. We’ll focus on gradual adaptation."
            hide player_image
            show Elena at left  with dissolve
            e "This may keep some governments in power, but at what cost? We might miss the crucial opportunity to act."
            hide Elena
            $ score +=1
            jump end

label end:
    scene bg_matrix
    player "Earth is in this situation due to your decision"
    hide bg_matrix
    if score >= 30:
        label ending_new_dawn:
            play movie "videos/best.webm"
            $ renpy.pause(5)
            scene bg_summit
            show Elena at left  with dissolve
            e "The emergency fund is established, allowing for immediate large-scale climate action. Countries begin deploying green technology and adaptation measures on a massive scale."
            hide Elena
            show Amara at left with dissolve
            a "This is the best possible outcome. The world begins to recover."
            hide Amara
            "The world rapidly transitions to renewable energy, and global warming stabilizes. The final scenes show flourishing cities powered by clean energy and communities thriving in harmony with the planet."
            jump credit
    elif score < 30 and score >= 15:
        label ending_age_of_struggle:
            play movie "videos/avg.webm"
            $ renpy.pause(5)
            scene bg_pedo
            show Elena at left  with dissolve
            e "Emergency actions save lives in the short term, but the lack of funding leads to limited impact. The planet is saved, but many struggle to adapt."
            hide Elena
            show Amara at left with dissolve
            a "We survive, but it’s not the future anyone hoped for."
            hide Amara
            jump credit
    else:
        label ending_collapse:
            play movie "videos/worst.webm"
            $ renpy.pause(5)
            scene bg_emergency
            show Elena at left  with dissolve
            e "The decision to delay radical action for political stability backfires. The planet reaches critical tipping points, and the future looks bleak."
            hide Elena
            show Amara at left with dissolve
            a "Entire ecosystems collapse, and the world struggles to cope with climate disasters."
            hide Amara
            jump credit
label credit:
    play movie "videos/credits.webm"
    $ renpy.pause(5)
    return