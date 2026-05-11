---
description: Transcription brute de la vidéo YouTube "Plan, Specify, and Implement with Spec Kit".
video_id: VfBLlAN5zdQ
url: https://youtu.be/VfBLlAN5zdQ
title: 'Plan, Specify, and Implement with Spec Kit'
author: 'Microsoft Developer'
language: en
auto_generated: true
duration: 35:52
fetched_on: 2026-05-11
---

# Plan, Specify, and Implement with Spec Kit

**Chaîne :** Microsoft Developer  
**URL :** https://youtu.be/VfBLlAN5zdQ  
**Durée :** 35:52

## Transcription

[0:01] [music]
[0:05] Hey Dan, how's it going?
[0:06] >> Hey James, good seeing you.
[0:07] >> It's good seeing you again. I see Master
[0:08] Chief is
[0:09] >> Master Chief. It's the holidays.
[0:12] >> We're ready. Let's do this.
[0:13] >> Ready.
[0:13] >> Uh well, let's get in our Warth Hog and
[0:15] let's ride, baby. Okay. If you know me
[0:17] and Den at all, we love just talking
[0:19] about uh everything including planning,
[0:22] specking, and doing real
[0:26] >> planning. real planning, real
[0:28] development on top of plans.
[0:30] >> Yes. I think so far today people have
[0:31] seen a lot of things with GitHub copilot
[0:34] with VS Code with Visual Studio, right?
[0:37] >> And often I think when we're demoing or
[0:39] we're actually writing software,
[0:41] >> we're just having an idea or a bug or
[0:44] assigning it and telling the agent what
[0:46] to do, right? And I was just meeting uh
[0:48] with a company and I said, you know, how
[0:50] I worked
[0:51] >> 2 months ago is so different to how I
[0:53] work now because I was doing what I just
[0:56] sort of described, which I had this idea
[0:58] in my head. I would write two or three
[0:59] sentences and let the AI figure it out
[1:01] for me,
[1:02] >> right?
[1:02] >> And there's pros to that, which is it
[1:04] went from my head into code pretty
[1:06] quick. But then there's a downside to
[1:07] that.
[1:08] >> And that downside often is that I
[1:11] haven't really given it the rails.
[1:13] haven't given it the the the plan, the
[1:15] spec on how to do it,
[1:16] >> right?
[1:17] >> Uh like I would normally get from my PM
[1:19] team that's assigning work uh our way or
[1:21] at least me assigning myself work,
[1:23] coming up with an idea.
[1:24] >> So plan mode inside of VS Code allows us
[1:27] to do a lot which is like I have an idea
[1:28] and turn it into a plan that I can then
[1:31] execute.
[1:32] >> When we think about spec driven
[1:33] development, that's a little bit
[1:34] different. And that's what we want to
[1:36] kind of talk about today. Yeah.
[1:37] >> Yeah. So what is spec driven development
[1:39] then? And why do people care?
[1:40] >> Yeah. So spectrum development is
[1:42] basically a practice like people think
[1:44] about it as some magical new thing right
[1:47] it's like oh it's all this agentic
[1:49] workflow and spec driven and it's all
[1:51] magic in reality it's essentially us
[1:54] formalizing the guard rails for AI
[1:56] models right because one of the things
[1:58] that if you talk to a lot of customers
[2:00] and they have tried vibe coding like all
[2:02] of us have right it's kind of exciting
[2:04] you start building things and you're
[2:05] like oh I'm going to tell the AI to
[2:07] build this website you start building my
[2:09] like the style and the buttons and the
[2:11] header and then you see it all light up
[2:12] and it's kind of cool. But if you start
[2:15] building production software, software
[2:17] that needs to be maintained by somebody,
[2:19] software that needs to evolve down the
[2:21] line beyond your initial prototype, that
[2:24] vibe coding approach doesn't really
[2:25] scale
[2:26] >> because the AI doesn't have necessarily
[2:28] the sense of taste or conventions that
[2:31] you need to be applying. So naturally,
[2:34] >> the model that you're using is going to
[2:35] make its own architectural choices,
[2:37] right? like it's going to decide to use
[2:39] a specific web framework if you didn't
[2:40] give it instructions. It's going to use
[2:42] a specific way to organize components
[2:43] and CSS and everything else. And that is
[2:47] problematic at scale because a lot of
[2:49] these decisions are not necessarily
[2:52] one-way doors like you can reverse them,
[2:53] but down the line once you build things
[2:55] out and then you realize that oh I want
[2:58] to add the shopping cart to my site and
[3:00] then you realize that the libraries that
[3:03] you use are now incompatible with some
[3:04] of the things that you're trying to
[3:05] build. So you start putting yourself in
[3:08] this corner where now you're like okay
[3:10] now I need to figure out a way out of
[3:12] this
[3:12] >> and spec driven development is a process
[3:14] by which we essentially frontload a lot
[3:17] of the thinking that you have to do and
[3:19] thinking with the help of LLMs right
[3:21] where you can say I am building an
[3:22] e-commerce site and I want to do X Y and
[3:25] Z and by the way my company is using
[3:28] Stripe for payments I'm using you know
[3:31] the Shopify front end for my store and
[3:34] you can assemble all these things
[3:35] together and a cohesive way and then
[3:36] have the AI help you build the things
[3:38] that you want to build in the way that
[3:40] also will scale in the future. So it
[3:42] essentially allows you to think first
[3:45] and get the outcome you want rather than
[3:47] offload that to the LLM itself to go and
[3:49] make the decisions for you.
[3:50] >> So I'm a developer now. I'm sort of want
[3:54] to live and breathe in the code, right?
[3:56] I want to live in my my repo. So how
[3:58] should I as a developer? I think that
[3:59] makes a lot of sense if I'm I'm like an
[4:01] architect or I'm a PM. But what if I'm a
[4:03] developer and I'm like okay I just want
[4:05] to write I want to jam on some code. How
[4:07] should I be thinking about spec driven
[4:08] development because maybe I'm a solo
[4:09] developer and I'm just like building and
[4:11] I want to build something or maybe I'm
[4:12] at a large enterprise or a startup or
[4:14] something like that. How should I as a
[4:17] >> engineer? Why is it important to me as
[4:18] an engineer to think spectrum and
[4:20] development?
[4:21] >> Well because one of the key pieces of
[4:24] data that you need for good software
[4:26] with the help of LLMs is context.
[4:29] >> Context on your codebase context on the
[4:31] decisions that you made. Right? Like if
[4:32] you throw an existing code base like
[4:34] let's say you take something as complex
[4:36] as VS code you know it's an open source
[4:38] project you go and you ask the LM to go
[4:40] and implement some feature it has no
[4:42] context as to like why did you decide
[4:44] the uh you know your status bar to be a
[4:47] certain color a certain style why did
[4:48] you decide the iconography to be a
[4:50] certain way right so the LM is going to
[4:52] start guessing
[4:53] >> when you have specs in place the LM can
[4:56] go and parse out and say okay let me
[4:57] look at how you've previously thought
[4:59] about styling okay now I understand well
[5:02] understand right but uh it essentially
[5:05] is going to look at it and have the
[5:07] context when you ask it to do other
[5:10] decisions around your product even
[5:12] though you're mostly in code but having
[5:15] that extra context is super helpful to
[5:16] make sure that any future code is going
[5:18] to be exactly what you wanted
[5:20] >> I see so in this instance once I've
[5:23] created some sort of infrastructure if I
[5:26] will
[5:27] >> then that infrastructure will continue
[5:28] to be followed yes now we have things
[5:30] like um uh custom instructions, agent MD
[5:33] files. How is this different? Because
[5:35] I'm hearing guard rails. I think about
[5:37] instructions and prompt files and those
[5:39] are my art own sort of guard rails.
[5:40] >> Yeah.
[5:41] >> When the agent is making code, how does
[5:43] this different than that?
[5:44] >> It actually uses a lot of them. It
[5:46] actually relies on a lot of them because
[5:48] specs themselves, if we think about the
[5:51] concept of spec development, there are
[5:52] certain artifacts that folks might have
[5:54] heard from previous videos and blog
[5:55] posts like we have the spec. MD file
[5:58] which is the specification that outlines
[6:00] the functional requirements for you're
[6:01] trying to build. There is the plan which
[6:04] is a technical plan. There is a set of
[6:07] tasks which is a broken down basically a
[6:09] list of things that allow LLM needs to
[6:11] execute to get you to the state that you
[6:13] want to get to. And all of these are
[6:14] just markdown files. And then you have
[6:16] agents.mmd to set up the uh instructions
[6:19] for the codebase which is by the way now
[6:22] supported by copilot
[6:24] uh the CLI. It's in VS code. You can use
[6:26] agents and dd everywhere.
[6:27] >> Everywhere,
[6:28] >> right? So, which is great. I love
[6:29] standards. I just love not to have to
[6:31] reimplement it over and over. But it it
[6:33] relies on a lot of these conventions and
[6:35] it basically assembles them together.
[6:36] Like this is what we launched, GitHub
[6:38] spec kit. And again, when I when I talk
[6:40] to people, they assume that this is like
[6:42] this magical product. Like it's just a
[6:44] bunch of prompts and scripts. All right,
[6:46] we just assembled them together to make
[6:48] it easy for folks to get started and see
[6:51] how they can leverage a lot of these
[6:52] spec driven workflows to build software
[6:55] in a more deterministic way than an LM
[6:57] typically could.
[6:58] >> Was this inspired like internally teams
[7:01] at Microsoft and GitHub or like where
[7:03] did it come about? Why did it come about
[7:04] like I think that sometimes like oh we
[7:07] built a thing but then like why did you
[7:08] build a thing?
[7:09] >> Okay. Yeah, that was actually a very fun
[7:11] story and I think I wish we had John
[7:13] Lamb here to to talk about this, but
[7:14] John is one of my colleagues who
[7:16] actually was the one that bootstrapped
[7:18] uh spec kit and a lot of the spec driven
[7:20] work inside Microsoft and the reason it
[7:22] was built is because John was using the
[7:24] clawed sonet models and as we both know
[7:26] sonet models can get a little bit
[7:28] overeager and you ask it to you know I
[7:30] want to build a website and it's going
[7:31] to go oh great let me write a whole new
[7:33] web framework first before you get build
[7:35] a website uh
[7:38] >> develops a programming language
[7:39] everything right
[7:40] >> the run time. Yeah.
[7:41] >> Exactly. And and using uh the spectral
[7:44] novel processes essentially set the
[7:46] guard rails for okay I want you to build
[7:49] X Y and Z only based on this plan.
[7:52] >> I see. And that's where it kind of
[7:54] started. But after that John quickly
[7:58] realized like oh there's actually value
[7:59] in this beyond. And this is where I work
[8:01] with him to like help productize this a
[8:03] little bit and then get it into the
[8:05] shape that we see now. Get our sweat
[8:06] kit. Well, I want to see it because it
[8:08] is one of the most popular repos on
[8:09] GitHub with over 53,000
[8:13] stars. Let's bring up your machine here.
[8:15] >> Yeah.
[8:16] >> And let's take a look. Okay, cool.
[8:18] >> 53.6,000.
[8:20] >> Hopefully more after a
[8:21] >> when we recorded our video for VS Code,
[8:25] how many stars was it?
[8:27] >> Like 24,000 or something like that.
[8:28] >> And that was not that long ago.
[8:29] >> No. Yeah. No,
[8:30] >> it's it's wild.
[8:31] >> People are loving it. Okay, so what is
[8:32] this? So, SpecKit itself, as I
[8:35] mentioned, it's in its core, all it has
[8:38] is just a bunch of prompts and scripts,
[8:41] >> okay?
[8:41] >> Like that that's all it is.
[8:43] >> Prompts and scripts.
[8:43] >> So, it's not like a uh it's not like a a
[8:45] package that you're like a like a npm
[8:47] package that you're installing. No,
[8:49] you're like you have to like you're not
[8:50] installing something into your project.
[8:52] >> No. Exactly. Because if you really
[8:55] wanted to like we have a helper CLI that
[8:57] I will show you in a second. It's called
[8:59] specify or specify, whichever way you
[9:01] pronounce it. uh you tell us uh but the
[9:04] CLI is actually not required because
[9:05] what you can do is you could go to
[9:07] releases you look at specit templates
[9:10] you just scroll scroll scroll
[9:13] >> and you find the agent that you want and
[9:15] the script language that you want like
[9:17] for example if I'm using codeex from
[9:18] openai I have a shell script or a
[9:20] powershell you can just download that
[9:23] right like if I get a powershell one and
[9:25] let's see let's download this let's
[9:27] let's pop it open
[9:30] and then we'll see it in a second that
[9:32] there is two folders in there. There's
[9:34] codeex that has a bunch of prompts,
[9:37] right? Specit, analyze, checklist,
[9:39] clarify, and so on. And we'll show you
[9:40] that in a second. And there's a bunch of
[9:43] metadata files like specified. There's
[9:44] scripts, there's some templates, right?
[9:47] Like again, it's all markdown files and
[9:48] scripts, nothing else. No batteries, no.
[9:51] >> And you said there's a bunch of
[9:53] different I'm seeing uh
[9:55] >> claw and kodakiler
[9:58] gemini. So, so this is really it's from
[10:01] GitHub, but it is you think of agent HQ
[10:04] like agents be everywhere. All agents
[10:06] can use this like an so it's almost a
[10:08] standardization but I'm assuming you've
[10:10] crafted them because these agents all
[10:11] work a little and require a little bit
[10:13] different setup.
[10:14] >> Right. Right. All right. They're a
[10:15] little bit different and also we are you
[10:18] heard it here first. We're working on
[10:19] spec kit v2. Well, that is going to
[10:22] remove the need for having these custom
[10:24] scripts per agent because it's all going
[10:27] to be bundled into specify CLI and it
[10:29] just like the agent will invoke, but
[10:30] we'll we'll we'll get to that. Um, but
[10:32] essentially when you are creating new
[10:35] projects with specify, you can you can
[10:37] install it and there is instructions if
[10:38] you go to the website and or the the
[10:40] repository here, you'll have
[10:42] instructions for using UV. We are big
[10:44] fans of UV if you're a Python developer.
[10:46] And that just happens because the
[10:48] specified CLI itself was written in
[10:50] Python, right? Like there's no Python
[10:53] requirement beyond this. Like you don't
[10:55] need to have it.
[10:56] >> Um, and again, you can install it. You
[10:58] can install it globally or for your
[11:00] instance. And then what you can do is
[11:02] you can do specify. Pump it up a little
[11:04] bit more for me. All right, let's do
[11:05] that. Beautiful. Let's let's let's clear
[11:07] it to make sure it's all aligned. Uh,
[11:09] all right. Nice. So specify and then
[11:12] init to initialize a new project. And
[11:14] then we're going to give it a project
[11:15] name. So we're going to call it test
[11:17] demo.
[11:19] So what's going to happen here is you'll
[11:21] see that again this was designed not
[11:23] with copilot in mind but with any agent
[11:26] in mind. So we have this uh beautiful
[11:28] ASKI arc here. Um and we have a
[11:31] selection of agent like what agent do I
[11:34] want to use and I can use my arrow keys
[11:35] because we use terminal interfaces as
[11:37] usual
[11:38] >> and I can pick any of them and all all
[11:40] this does is downloads the templates
[11:42] that I want. We're going to use copilot
[11:43] because of course we're going to be of
[11:45] showing copilot and then I'm being
[11:47] prompted to enter the shell that I'm
[11:48] going to be using. If I'm using
[11:50] PowerShell on Linux, you can use
[11:51] PowerShell on Linux. If you use shell
[11:52] scripts, you can use shell scripts. I'm
[11:54] going to use PowerShell. Just going to
[11:56] download it. Boom. Done. And all this
[11:59] did is basically just the the releases
[12:01] that you saw, the zip files that you
[12:02] saw, it just pulled them locally,
[12:03] extracted them, and made it ready for
[12:05] your project.
[12:06] >> That's it. So, we can go to our folder
[12:08] for test demo. And let's take a look
[12:11] here. If I look at inside the folder and
[12:13] I have the GitHub.specified vscode
[12:16] because copilot we designed it around VS
[12:19] Code.
[12:19] >> Got it. Okay. Now, here's one question
[12:21] for you. You did this in a brand new
[12:23] folder.
[12:23] >> Yes.
[12:24] >> Right. Because you're like, "Oh, I'm
[12:25] brand new project." And probably the
[12:27] majority of people watching this and
[12:28] streaming this in right now are like,
[12:31] >> I have an existing project.
[12:32] >> Yeah.
[12:32] >> Then like how do I do I add this to do I
[12:35] do the same thing on, you know, my web
[12:37] app on my solution? What do I do? For
[12:39] example, let's go just back just one
[12:41] folder and we're going to create a new
[12:43] folder test demo existing
[12:47] and we're going to go to cd test demo
[12:49] existing
[12:51] and here now I can do specify in it and
[12:54] I can do either here or just use the dot
[12:58] just that's it boom
[13:00] >> so and this is going to bootstrap the
[13:02] project in the current folder. So if I
[13:04] do again same workflow it's all console
[13:06] based you don't actually need to go
[13:07] through this interface it completely can
[13:09] be automated by using parameters or
[13:12] arguments in the terminal but I just
[13:14] happen to like the the two so I can show
[13:16] you how to how to navigate it but
[13:17] >> so this so this is nice and I want to
[13:19] point out that is because a lot of times
[13:20] we get the questions which is like hey
[13:22] yeah I'm already in an existing app
[13:25] right does spec kit make sense for me
[13:27] >> yes
[13:27] >> even if I already have an app that I've
[13:29] been maybe releasing in to the wild for
[13:32] years
[13:32] >> absolely Absolutely. Absolutely. You can
[13:35] use it with existing project. I have a
[13:37] YouTube video for it, too.
[13:38] >> Oh, nice. We'll link to that.
[13:39] >> We'll link to that. But, um, so we have
[13:41] our test demo project and here I can
[13:42] just start VS Code right from the
[13:44] folder. So, we'll see this uh light up
[13:47] in our Visual Studio Code instance.
[13:50] We're going to make this full screen and
[13:52] let's zoom in just a little bit.
[13:53] Beautiful. Just a little bit all the
[13:55] way.
[13:55] >> But notice certain things here. So, when
[13:57] we started that now there's suggested
[14:00] actions here.
[14:01] >> See this? So I don't as a developer
[14:03] because we have the GitHub specify all
[14:05] these folders that we talked about. We
[14:07] now have a suggested action for me to
[14:09] get started. I don't need to guess
[14:11] what's the command. I say oh
[14:12] constitution the constitution is a
[14:14] starting point. The whole idea behind a
[14:16] constitution with specit is that there's
[14:18] a set of non-negotiable principles for
[14:21] your project. We're actually in spec
[14:23] merging that into agents.mmd. So it's
[14:25] not going to be a constitution but for
[14:26] now there is. And the the purpose of
[14:28] this is to make sure that whatever
[14:30] decisions you make down the line for
[14:31] your project, for your functional spec,
[14:33] technical spec, the tasks, you're always
[14:35] following specific requirements like I
[14:37] always want to deploy to Azure. I always
[14:40] want to make sure that the packages that
[14:41] this tool is going to use are Azure
[14:43] specific and not pulling some other
[14:45] cloud provider, right? Because this
[14:46] where I'm deploying things. So
[14:48] establishing the constitution is very
[14:49] important. So in our example like we can
[14:51] do something like if I'm building let's
[14:53] say a um podcast website right I can
[14:57] just say it's a static website
[15:00] with minimal dependencies
[15:04] right like we we can make it more
[15:06] complex.
[15:07] >> Yeah.
[15:07] >> But I think that that's a good starting
[15:09] point.
[15:10] >> Now are you specifying
[15:12] like what technologies you're using
[15:13] because this is okay this is just
[15:15] generic like
[15:16] >> this is this is very generic. Right. And
[15:18] notice that also in the latest version
[15:19] of specket, we use the agent switcher.
[15:23] >> So for every instruction here, every
[15:26] command, we're actually using custom
[15:28] agents.
[15:29] >> Oh, I see. I can see it down here in the
[15:31] bottom that it it automatically switched
[15:33] Yeah.
[15:33] >> to this agent. So that would that means
[15:35] that it kind of works everywhere. If
[15:36] you're on GitHub, you you actually you
[15:38] could use the same exact agent. So it's
[15:39] not just like a prompt.
[15:40] >> Yes. Exactly.
[15:41] >> Very cool.
[15:41] >> And the the agent itself is going to
[15:43] invoke a prompt. Okay. for constitution
[15:46] and then it's going to run all the
[15:47] scripts that it needs to be. But this
[15:49] allows us to do things like handoffs,
[15:52] >> right? Where once the constitution is
[15:54] finished, I can say, "Oh, and now go
[15:55] write the spec. Oh, and now go do the
[15:57] technical plan and kind of jump around,
[15:59] right?" So again, for a lot of the
[16:01] things that you see here with the
[16:03] constitution and the the spec creation
[16:06] and design that we're going to see
[16:07] later, all of this can be done manually.
[16:10] >> Like you don't actually need to use
[16:13] specit for this. you can just manually
[16:15] type the commands but like
[16:17] >> come on we can do we can do better than
[16:19] that right so um
[16:21] >> here's a good question for you if I was
[16:22] in an existing project let's say I had
[16:24] an existing blazer web app or react you
[16:26] know application could I say hey
[16:29] >> go like look at this project and then
[16:31] create the constitution based off of
[16:33] what I have
[16:34] >> absolutely you could you can absolutely
[16:35] do that and this is when you saw me kind
[16:37] of prompt it you could totally ask it to
[16:39] just like go and first inspect the
[16:41] project
[16:42] >> and then give me the content I Gotcha.
[16:44] >> So, and notice that now it provides me a
[16:45] handoff, right? Like proceed from spec
[16:47] constitution build specification.
[16:49] >> Beautiful.
[16:50] >> So, the shout out to VS Code team who
[16:52] actually implemented this.
[16:52] >> Yeah, it's really neat.
[16:53] >> Very similar if you're using plan mode.
[16:55] It's like I create the plan then I do
[16:56] the next thing. You pull man hand off
[16:58] XYZ.
[16:58] >> Right. So, what's in this constitution?
[17:00] >> So, what's in the constitution? Let's
[17:01] hide chat mode for a second. So, we'll
[17:03] see that it has a definition for static
[17:05] website, right? So, minimal
[17:06] dependencies, great requirement. Static
[17:09] first also great requirement. I love it.
[17:11] simplicity, complexity must always be
[17:14] justified and yagney.
[17:16] >> There you go.
[17:16] >> Yeah, there we go. Um there's some
[17:18] performance standards and
[17:21] there's also this misconception that oh
[17:23] you use these commands it creates these
[17:24] artifacts and this is like ah now I have
[17:26] to go to chat and start like asking you
[17:28] to change things. It's a markdown file.
[17:30] >> Yeah.
[17:30] >> Just just go change it yourself. Like
[17:32] you don't you don't want the the
[17:34] >> change 3G to LTE and
[17:35] >> Right. Exactly. like or you know like
[17:37] things like governance or things like
[17:40] development workflow if you see like oh
[17:41] I actually don't want to test against
[17:43] Safari because I'm just remove it.
[17:45] >> What else would go in here Dan? Like you
[17:47] know it did some performance stuff like
[17:48] you know you very simplified but when
[17:50] I'm thinking about as a developer what
[17:51] else would I think about maybe I might
[17:53] want to add in in my own constitution
[17:55] here
[17:56] >> things that you want to be
[17:57] non-negotiable for your project.
[17:59] >> Right? So if you want like every
[18:01] developer that touches this project, I
[18:02] want to make sure that you're always
[18:03] using the latest version of TypeScript.
[18:06] This is where you go. I want to always
[18:08] use this particular package for logging.
[18:11] This is where it goes. Right? Like
[18:12] things that you want to make sure that
[18:14] are consistent across the project.
[18:15] >> I see. Got it. Okay. And that can
[18:16] include both technical requirements and
[18:18] non-technical requirements.
[18:19] >> I see. Gotcha. In this case, there's not
[18:21] a lot of technical requirements. There's
[18:23] kind of there's performance stuff, but
[18:25] it's not like talking about frameworks
[18:26] or this. It does talk about lighthouse
[18:27] performance, things like that, which is
[18:28] kind of nice. Uh, but so I'd be like,
[18:31] hey, always make sure I'm on the the LTS
[18:33] release of this thing of node orn net or
[18:35] something like that. And that's that's
[18:36] where I would specify this here.
[18:38] >> Or for example, if I want to say like
[18:39] it's a static site and I want to make
[18:40] sure it's always built with Hugo.
[18:42] >> Ah, got there you go. Like you can just
[18:44] say that.
[18:45] >> All right.
[18:45] >> But uh we're going to go to the chat and
[18:46] now I can click the build specification
[18:48] and notice that it's switched my agent
[18:50] to specit.specify command. Yes. Or the
[18:53] specify agent. And we can I'm just going
[18:55] to remove this placeholder here. And we
[18:56] can just say I want to build a podcast
[18:59] website
[19:01] with featured episodes
[19:07] >> like that,
[19:07] >> right? So minimal format again. And
[19:10] notice that also as I type this in, I
[19:12] enter the command. Now it gives me
[19:14] handoffs for other steps like I can
[19:17] build a technical plan or I can clarify
[19:19] spec requirements which is very
[19:21] important and we'll we'll get to that
[19:23] because we recognize the fact that once
[19:25] you build specifications like the we
[19:27] just oneotted it here like oh I'm going
[19:29] to ask the command to go and build the
[19:30] spec document and we're going to have
[19:32] the document here in a second but that
[19:34] on itself is not enough.
[19:36] >> I might be missing something. I might
[19:38] not know something that I required it to
[19:41] go and design in a way that I did not
[19:43] intend to. Under specification is also a
[19:46] problem.
[19:47] >> So here you've you know green field it
[19:49] here. So you said here I'm going to
[19:50] build this website.
[19:51] >> Yeah.
[19:52] >> Um
[19:53] >> again I think about this existing
[19:55] application that I may have. Um should I
[19:58] like retroactively go back and create
[20:00] like a default specification for what
[20:02] the app is first or should I think about
[20:05] should I break it down into features?
[20:06] Like for example here you're like yeah I
[20:08] want to create this page featured
[20:09] episodes should I should I think about
[20:12] it of
[20:13] >> this first even if I'm creating and
[20:14] going for the first time should each
[20:16] sort of uh fe specification be a feature
[20:21] like hey I'm creating a podcast website
[20:22] so create just the base website and then
[20:24] I'm going to have another specification
[20:26] for um episodes another one for guests
[20:29] another one for is that how I think
[20:30] about or should I try to oneshot
[20:32] everything in one huge specification
[20:34] first
[20:34] >> I think from my experience and us
[20:37] running this spec for a while with
[20:39] different projects.
[20:40] >> Mhm.
[20:40] >> The workflow you described probably
[20:41] would work best.
[20:42] >> Okay,
[20:43] >> that is and the reason for that is very
[20:44] simple is because you want to make sure
[20:46] that you chunk the context, right? When
[20:49] you start to kind of offload everything
[20:51] into one like it it could work, but then
[20:54] you have to be somewhat hands-on or have
[20:56] basically like an agent fleet to go and
[20:58] like check each other and be like, "Oh,
[21:00] is this right? Is it rendering
[21:01] correctly?" Versus start minimally. But
[21:03] also we'll get to that because for
[21:04] Greenfield projects what we've actually
[21:06] done is at the spec stage because here
[21:09] I'm building a whole new podcast
[21:11] website. It's an end to- end thing,
[21:13] right? Um, we make a lot of assumptions
[21:16] and we make a lot of experience pieces,
[21:19] but it's very hard to dissect from it.
[21:21] Like what exactly is the minimal product
[21:23] that I want? The MVP, right?
[21:24] >> Yeah. Yeah.
[21:25] >> But once we get to the last stage of
[21:27] tasks, we are actually smart about
[21:30] identifying what needs to go into the
[21:32] MVP and start with that and then
[21:34] incrementally build on top of it.
[21:36] >> So, you don't actually have to do that
[21:37] decision yourself.
[21:39] >> Well, let's take a look at the spec real
[21:40] quick. So, you created a new specs
[21:41] folder. We have our spec.mmd in our
[21:45] feature folder 001 podcast website. So,
[21:48] we're going to look at spec.md. I'm
[21:49] going to close the terminal and we're
[21:50] just going to keep all these changes
[21:53] because we just going to blindly trust
[21:55] the AI. So, notice that it broke it down
[21:58] for me in user story. So, I have browse
[22:00] featured episodes and landing page.
[22:02] Great. It has some scenarios. If you're
[22:04] a product manager, these might seem
[22:06] familiar.
[22:06] >> Love this.
[22:07] >> Uh you episode details. Great. Like
[22:10] notice I did not specify that I want to
[22:11] view episode details, but it just kind
[22:12] of assumed because you're building a
[22:13] podcast website. I kind of need it.
[22:15] >> And this is kind of interesting too
[22:16] because it's it's saying like do you
[22:17] want to even play episodes? It's going
[22:19] to assume that you want a audio player.
[22:20] So you may not. So you might want to
[22:22] edit that right in that instance.
[22:24] >> And this is the the interesting part. So
[22:25] we have the edge cases here and all the
[22:27] functional requirements. Notice that it
[22:28] broke it down into way that I can easily
[22:30] see them and see exactly what needs to
[22:32] be. But let's say that I read through
[22:34] this and say, "Oh, this this sounds
[22:36] reasonable. This sounds great." Yeah.
[22:37] Like, but
[22:38] >> I don't actually know what I don't know.
[22:40] >> Yeah.
[22:41] >> So, this is where we use clarify.
[22:43] >> I never know what I don't know.
[22:44] >> I never know what I know.
[22:45] >> So, we're going to use the clarify
[22:46] command. I just onecllicked it and it
[22:48] just bootstrapped the clarify agent with
[22:50] the clarify command.
[22:52] >> And what this is going to do, it's going
[22:53] to use the LLM again, use the model to
[22:56] look over the spec and then start
[22:58] thinking through like what are the
[23:00] things that are missing,
[23:01] >> right? And we kind of see this here
[23:03] where it created this table for us. that
[23:05] says coverage. Oh, there we go.
[23:08] >> That's my new favorite button. Yeah,
[23:10] >> today I learned. There you go.
[23:11] >> That's a great button.
[23:12] >> I love it.
[23:13] >> Um, so we see this table that I created,
[23:15] right? So like, oh, you have things like
[23:18] core user goals, they're pretty clear,
[23:20] like, okay, makes sense. Things that are
[23:22] out of scope are not defined. Things
[23:24] like user roles and personas not defined
[23:27] because, oh, hey, visitor like is this a
[23:30] new versus returning? Is it a podcast
[23:31] owner because you're right, which makes
[23:33] sense. It's a podcast website. Uh,
[23:36] identity and uniqueness rules, all the
[23:38] stuff that's missing here, which is
[23:40] like, yeah, I like this. And then it
[23:44] starts asking me questions. I like that.
[23:46] We limit it to five questions to start
[23:48] just because we want to make sure that
[23:50] we don't overwhelm you too much. But
[23:53] it's actually going to ask the question
[23:55] itself. So, how will episode data be
[23:57] managed and added to the website? And it
[23:59] recommends you an option,
[24:01] >> but also it gives you other options. Oh,
[24:03] nice.
[24:04] >> Right. So, it's like, oh, you can import
[24:06] things from an RSS. You can static JSON
[24:08] define things. And I think option B
[24:10] makes sense. So, I can just literally be
[24:11] lazy and say B.
[24:13] >> Oh, it's going to do one question at a
[24:14] time. Oh, nice. Interesting. Okay.
[24:16] >> I've recorded this answer. I like it.
[24:18] Okay, cool.
[24:19] >> Because it not only records the answer,
[24:21] but actually goes into the spec and it
[24:23] adds it.
[24:24] >> So, see it says clarifications and it
[24:25] has a session from today.
[24:27] >> Nice.
[24:27] >> And it's gonna Oh, okay. Let me add this
[24:29] to the plan. And then it's gonna like
[24:30] let's look at the changes. And it
[24:32] actually added the requirement here.
[24:34] >> Oh, nice.
[24:35] >> Now it jumps to the second question
[24:36] here, which is like what is the expected
[24:38] episodes catalog size this website needs
[24:40] to support? And it's like 10 to 50
[24:42] episodes. I like D. I wanted this to be
[24:45] a popular podcast, so I'm going to use
[24:47] the 200 episodes.
[24:48] >> Podcasting forever,
[24:49] >> right? So you can be lazy and answer
[24:51] these with just one letters or you can
[24:53] give a short answer yourself. So you can
[24:55] say, actually, none of this is correct.
[24:57] Yeah. Uh, so you can kind of go through
[24:59] the the the steps here and we're not
[25:00] going to go through all the five
[25:01] questions because you get the idea, but
[25:03] like it it questions you and makes you
[25:05] rethink the assumptions that you have
[25:07] because it it's your step of like ask me
[25:10] questions about this and see what you
[25:12] say.
[25:13] >> This is my favorite part of plan mode
[25:14] when I'm thinking about planning just
[25:16] like a small implementation, right? In
[25:17] this instance, we're planning like
[25:19] bigger things as well and you could be
[25:20] planning things in plan mode. But I love
[25:22] the questions cuz it's thinking of
[25:24] things that I would have never thought
[25:24] of. Maybe I would have thought it but I
[25:26] just wouldn't have put it into a prompt
[25:27] to like fire off and even to create.
[25:29] >> Exactly.
[25:29] >> Yeah. So once we're good with the spec
[25:32] we can build a technical plan and this
[25:34] is
[25:35] >> where we are establishing the technical
[25:37] requirements.
[25:38] >> So I can just say I am building with
[25:41] Hugo because I want a static site.
[25:42] >> You love Hugo
[25:43] >> and I can just add it you know like
[25:45] Tailwind CSS
[25:48] for styling.
[25:51] I don't know you can use any other
[25:53] libraries. But basically this this is
[25:55] where you come in and add all the
[25:57] technical requirements that you want to
[25:58] have for your project all of them. And
[26:00] the more detailed the problem the better
[26:02] right like you want to avoid the LM
[26:04] making assumptions
[26:05] >> and in this case again if you're in an
[26:06] existing application you have the
[26:08] technical
[26:09] >> correct
[26:10] >> because you you have the project so you
[26:12] just say go look at it figure it out.
[26:13] >> Exactly.
[26:14] >> And then review it to make sure and you
[26:16] might find some things maybe aren't what
[26:18] you expected.
[26:19] >> Right. Right. Right. Exactly. I notice
[26:21] also that VS code smartly enough does
[26:23] that it it has this kind of a set of
[26:25] stages that it goes through right
[26:27] because my my planning has several
[26:29] stages to it like I needs to generate a
[26:31] research file data model the contracts
[26:33] the quick start
[26:35] >> and so it's going to go and do all of
[26:36] this plan or setting the technical
[26:39] details is probably the more time
[26:41] consuming part of this
[26:42] >> gotcha it's gonna
[26:43] >> it's going to go and think a lot
[26:45] >> it's going to go and think
[26:46] >> now you also are using a opus model here
[26:48] when you are thinking about these
[26:50] different tasks. Do you just kind of
[26:51] stick with one model? Do you move
[26:53] around? I mean uh there's new models
[26:55] every week, every day,
[26:57] >> you know, like how are you think about
[26:58] this? Because uh I was just did a
[27:00] >> a recording for the VS Code podcast with
[27:02] Julia
[27:03] >> and we're talking about the exact same
[27:05] thing. What model use when XYZ for these
[27:07] different
[27:07] >> scenarios? It it really depends on your
[27:09] mood uh or well okay there there's more
[27:12] to that of course but it it depends on
[27:14] what you're trying to do. I am
[27:15] personally a fan of the anthropic models
[27:17] like the cloud models because they're
[27:19] much more I would say creative and much
[27:23] more like oh you're writing a spec
[27:24] document let me think through the
[27:26] various things that you can include in
[27:27] that spec. I think
[27:28] >> GPD5 for example can be a bit more
[27:31] reserved like it's not going to go as
[27:32] far about giving you all the options and
[27:35] it can actually sometimes interrupt and
[27:37] like oh it's I wrote this section for
[27:39] the spec. Would you like to me to
[27:41] continue thinking about the spec and
[27:42] like I I just don't like that. I I I let
[27:45] Claude like either Opus or Sonnet just
[27:47] go and run with it and then I can always
[27:50] interfere and then say nope stop let's
[27:52] do something else. Um but ultimately it
[27:54] depends on also scenarios like I've seen
[27:57] uh a lot of the sonnet models be really
[28:00] really good with C# code for example
[28:02] >> and GPD5 is like can hit or miss right
[28:06] but if you use GBD5 at TypeScript it's
[28:09] somehow better.
[28:11] >> So you have to try this out by yourself
[28:13] and then see
[28:14] >> see what it does. Yeah, and that's kind
[28:15] of the cool part is it's going to be
[28:17] part of your source code and I saw it
[28:19] created a branch automatically so you
[28:21] could always
[28:22] >> be committing rolling back as well if it
[28:25] wasn't
[28:25] >> exactly right and this actually
[28:27] something that we're looking at adding
[28:28] in spec v2 where you can autocommit
[28:30] things because we're already on a branch
[28:32] as it goes to different stages and you
[28:34] go from spec technop plan it commits it
[28:36] so then you can say nope never mind
[28:37] revert it back now I will also add that
[28:41] something that I love about the fact
[28:43] that you have this spec driven workflow
[28:46] in place in a repository is that it
[28:48] allows you to build multiple
[28:51] implementations,
[28:52] >> multiple variations. Like let's say
[28:53] we're building a podcast website right
[28:55] now and notice like I could have stopped
[28:57] at the spec and not even go into the
[28:59] plan and say I want to have one with
[29:01] Hugo
[29:02] >> but the other one what if we use Nex.js
[29:05] with a stat static
[29:07] >> site rendering.
[29:07] >> Yeah. What would that look like?
[29:08] >> What would that look like? And not just
[29:10] that, but maybe you want to compare the
[29:11] performance. I want to make sure like
[29:13] which one is faster, which one is going
[29:14] to be like better suited for my specific
[29:18] cloud provider. And if you have just one
[29:21] spec, you can easily fork that and start
[29:24] implementing like two, three, four, five
[29:26] different variations with Saab agents.
[29:28] >> Yeah.
[29:28] >> Right. Uh and they can create their own
[29:30] branches and you can use git work trees.
[29:32] Magical feature by the way. Uh everybody
[29:35] should be uh aware of git work trees.
[29:37] >> Yeah. But uh yeah, this is I I think
[29:40] this is the the thing that is really
[29:42] really going to change how how we work
[29:43] is that a lot of the workflows around
[29:45] spec driven development are heavily
[29:49] leaning into git based operations.
[29:52] >> And if you know git and you can use like
[29:54] this quick like oh did not like the spec
[29:56] revert back
[29:57] >> revert back
[29:57] >> right and and agents modern agents are
[30:00] really really good at operating on top
[30:01] of git. Yeah, I like that idea, too.
[30:03] When we're answering questions earlier
[30:04] on, there's a lot of different
[30:06] selections. You might in your mind say,
[30:07] "Okay, actually, I want to do another
[30:09] version of this with different answers
[30:11] to those and then be able to actually
[30:13] refine them in general."
[30:14] >> Right. All right. You you because you're
[30:16] not binding yourself to a specific
[30:18] implementation with the spec.
[30:20] >> Spec is detached from technical details.
[30:21] >> I see.
[30:22] >> You are able to essentially come in and
[30:24] say, "I want this to look different. I
[30:26] want this to be implemented with a
[30:27] different stack."
[30:28] >> It still binds itself to the
[30:30] constitution. So if you have like
[30:31] non-negotiables like it's it still needs
[30:34] to deploy to Azure successfully. I'm not
[30:36] going to say minimal stat
[30:39] >> but it gives you the ability to then
[30:40] fork off basically and then go and each
[30:43] iteration can work independently
[30:46] and you can see the outcomes of each and
[30:49] then decide which of them are more
[30:52] suited for you trying to do.
[30:53] >> That's very cool.
[30:54] >> Yeah.
[30:54] >> All right then. So what's the next step
[30:56] here? So now it's creating these uh
[31:00] requirements, checklist, what all what
[31:02] all is happening here?
[31:03] >> Yeah. So it's going to create the plan.
[31:04] It's going to give us technical details.
[31:06] And then the last stage here is just
[31:08] tasks. It's going to break things down
[31:10] into individual tasks. And uh you can
[31:12] watch some of the past videos. We'll
[31:14] have documentation for this. But you'll
[31:16] essentially have a broken down list of
[31:18] tasks that the LM can one by one proceed
[31:21] and implement. I see.
[31:22] >> And some of them can be parallelized.
[31:24] So, um, yeah, that's essentially the
[31:27] flow. That's the the gist of Spec Driven
[31:29] with SpecKit. We try to make it very
[31:30] straightforward. Like, there's only a
[31:32] handful of commands that you can just
[31:33] use and be on your merry way.
[31:36] >> All right. Well, before we get out of
[31:37] here, I do want to tap really quick on
[31:39] to the generated code in here. So, let's
[31:42] bring your your machine back up here
[31:44] because it's really close. It's on 80 of
[31:45] 8. So, if we open up, you know, this
[31:48] folder for this production, I want to
[31:50] kind of walk through really quick. We
[31:52] have the requirements. We have
[31:53] contracts, we have data models, and a
[31:56] plan. Can we just open them up really
[31:57] quick?
[31:57] >> Yeah, of course. So, let's Yeah, let's
[31:59] close the chat here. Let's close the
[32:01] terminal. Let's take a look at the I'm
[32:02] just going to keep the changes. And I'm
[32:04] actually we're going to use a chat and
[32:05] keep all of them so it's easier to parse
[32:07] that.
[32:08] >> Uh, but if we look at the plan, notice
[32:10] that it has a technical context. It
[32:11] actually structured based on a template
[32:12] that says okay it needs to use go
[32:14] templates because we're using Hugo with
[32:16] HTML 5 some dependencies target platform
[32:19] how we test things the scale the
[32:22] constitutional check that I mentioned
[32:24] right very important not to not to be
[32:25] missed uh because it made sure that okay
[32:28] whatever I generated does it fit the
[32:30] requirements to define a constitution
[32:31] minimal dependency static for simplicity
[32:33] perf and development workflow so it
[32:35] passed so it can continue it outlined
[32:37] the structure of like how is the content
[32:39] going to be laid out M this is great
[32:41] like I love this the archetypes the
[32:43] assets the content itself in the episode
[32:45] subfolder so this is great um all these
[32:48] details are now captured in the plan and
[32:50] again I can modify them if needed uh the
[32:52] data model itself it defines for example
[32:55] the entities are operating with because
[32:56] they're podcast like here's the podcast
[32:58] episodes right and like which of them
[32:59] are required which of them are not
[33:01] >> which again is very very convenient for
[33:04] us to manage this correctly and if
[33:05] anything stands out you can you can
[33:07] change it research is a very important
[33:10] one Because if you are using agents like
[33:12] claude code, it'll actually go out on
[33:15] the web and research. And we can
[33:16] probably use beast mode from our friend
[33:18] Burke.
[33:18] >> Yeah.
[33:19] >> To go and and do this. But right now,
[33:21] because it did not do this in VS Code,
[33:23] it basically research it from the corpus
[33:24] of data that it has.
[33:26] >> Very cool.
[33:26] >> In a training, right? But it actually
[33:27] looked and said like, oh, okay, what's
[33:29] the best way for me to do front matter?
[33:31] Okay, like this is the format for an
[33:33] episode. Like, okay, great. So, key
[33:35] findings and document all this stuff.
[33:36] Tailwind CSS integration with Hugo.
[33:38] Like, how do I do that? like, okay, I
[33:40] should probably use an npm build step
[33:42] for this. Makes sense. So, all the stuff
[33:45] is captured. All the stuff is now like
[33:47] because it's in a folder, the 001
[33:49] podcast website, this means that this is
[33:52] the context that I can operate on. So,
[33:54] down the line after this podcast website
[33:56] is implemented, if I ever need to go
[33:57] back and change something, it now has
[33:59] the historical like
[34:01] >> what did you think about like the data
[34:02] model for podcast episodes? How is the
[34:04] configuration done? What are the where
[34:06] are episodes located? This is how
[34:09] context.
[34:10] >> So then we create the tasks and at that
[34:11] point is it just implementing it just
[34:13] like we would normally like at at this
[34:15] point if you go and create the task it's
[34:16] just going to go like I didn't need to
[34:18] type anything. I just clicked the button
[34:19] and it's going to just break this down
[34:21] based on the plan the spec and all the
[34:23] details and create a tasks.mmd file.
[34:27] It's just going to have the list of
[34:28] tasks and then at that point you just
[34:29] ask it to go and implement this.
[34:31] >> In fact there's a button for it.
[34:32] Implement
[34:32] >> implement. Yes. Um
[34:34] >> and you could fire that off in a
[34:36] background agent or anything you want to
[34:37] work. Very cool. So this is nice because
[34:39] you got that really super human in the
[34:41] loop understanding going through the
[34:43] requirements going through the
[34:44] specification going through the plan
[34:46] implementation not for for the first but
[34:47] for existing for every new feature. So
[34:50] now we're going to add a guest page. We
[34:51] do the same thing we created. It'll be a
[34:53] 002 then right.
[34:54] >> Yes. Yeah. Exactly. It's going to
[34:55] increment these and then if you want to
[34:57] add any capabilities you go through the
[35:01] the process that we just showed you. You
[35:03] don't need to create a constitution
[35:04] because it already exists. You can just
[35:05] go straight into spec.
[35:07] >> Yeah.
[35:07] >> And just go from there.
[35:08] >> Very cool. Den, this is awesome. We will
[35:11] to put this up in on demand. We'll put
[35:13] links into the show notes and all that
[35:14] stuff. Maybe we'll figure out some way
[35:15] of putting Den's YouTube on here. And we
[35:17] actually have some great videos on the
[35:18] the GitHub and the VS Code YouTube as
[35:21] well. Just look for SpecKit basically
[35:23] and and we'll go to the the GitHub
[35:24] github.com/githubspec-kit
[35:27] and you'll find a bunch of videos there.
[35:28] Dan, thanks so much for coming and
[35:29] showing us this off. I really appreciate
[35:30] it.
[35:30] >> Thank you.
[35:31] >> Awesome. All right, back to Katie and
[35:33] Christina as we go into our next episode
[35:36] or next session, whatever it is. What
[35:37] are we doing? What are we doing here?
[35:39] Sessions. Sessions. I'm in podcast. I'm
[35:41] in podcast mode. All right. Thanks, Den.
[35:44] And let us know and follow up in the
[35:45] Discord and ask questions in the chat
[35:47] and we'll have Den follow up as well.
