---
description: Transcription brute de la vidéo YouTube "Pi Coding Agent (Free Course)".
video_id: BZ0w0JhPQ9o
url: https://www.youtube.com/watch?v=BZ0w0JhPQ9o
title: 'Pi Coding Agent (Free Course)'
author: 'Owain Lewis'
language: en
auto_generated: true
duration: 28:01
fetched_on: 2026-05-03
---

# Pi Coding Agent (Free Course)

**Chaîne :** Owain Lewis  
**URL :** https://www.youtube.com/watch?v=BZ0w0JhPQ9o  
**Durée :** 28:01

## Transcription

[0:00] This video is a full course on the pie
[0:01] coding agent. By the end of the video,
[0:03] you'll know everything you need to know
[0:04] about using this tool and you'll be able
[0:06] to make a decision about whether this
[0:07] belongs in your AI coding workflow.
[0:09] [music]
[0:10] So, pie is an open source agentic coding
[0:12] agent. If you've used Claude code or
[0:13] code next, you know exactly what this
[0:15] is.
[0:16] But, pie has a radically different
[0:17] approach to most [music] other coding
[0:19] agents. It ships with just four tools.
[0:21] It works with all AI models and it has a
[0:23] system prompt that is less than 1,000
[0:25] tokens. You can customize and it has a
[0:27] really interesting extension system that
[0:29] lets you change anything about this
[0:30] agent. In this course, we'll cover
[0:32] installation and setup, daily usage, how
[0:34] to configure custom providers and system
[0:35] prompts, how to build your own
[0:37] extensions and how to build skills for
[0:39] repeatable [music] workflows. I'll also
[0:41] give you an honest comparison against
[0:42] other AI coding tools [music] so that we
[0:44] can see how they stack up. So, let's get
[0:46] into it. Okay, so the first thing we
[0:47] want to do is [music] get the agent set
[0:49] up and installed. So, what we're going
[0:50] to do is go to pi.dev and then we're
[0:54] going to copy this one install command.
[0:56] Once you have that copied, you can move
[0:58] over into your terminal and you can just
[1:00] paste in that command and it should set
[1:02] everything up for you. I already have
[1:03] this installed. So, it won't do
[1:05] anything, but if you don't, this will
[1:07] get it all set up. All right, perfect.
[1:08] So, now the agent is installed. So, what
[1:10] we can do is type the word PI or pie and
[1:14] it will start up the coding agent. So,
[1:16] the first thing you're going to want to
[1:17] do is choose a model provider. So, we're
[1:20] going to type login and you'll see here
[1:22] there's a bunch of different OAuth
[1:23] providers. We have the OpenAI chat GPT
[1:27] subscription, which I'm using currently.
[1:30] You can also use Google Cloud or GitHub
[1:32] co-pilot. You also have Anthropic there
[1:34] as well. It is worth noting that with
[1:36] Anthropic, you're not able to bring your
[1:38] paid subscription in. So, this is one of
[1:41] the biggest problems for me personally
[1:42] because I do use a subscription a lot.
[1:44] So, if you use this option, Anthropic
[1:47] recently banned this and so this will
[1:49] use your extra credits, essentially your
[1:52] API tokens. So, if you want to use
[1:54] Anthropic models, you have to use an API
[1:56] key essentially and so it's going to be
[1:57] more expensive than using it through a
[2:00] subscription. Okay, so once we have our
[2:02] provider selected, so for me that's
[2:04] OpenAI, you can type /model and then you
[2:07] can choose the AI model you want to use.
[2:09] I'm using the 5.3 codex model and you
[2:13] can see down here the model is also
[2:15] listed here. And you can also see that
[2:18] I've set it to high reasoning as well.
[2:21] Another good option is a tool called
[2:23] open router.
[2:25] So, open router is a way of getting
[2:27] access to pretty much every single AI
[2:29] model all from one single API. But, in
[2:32] order to use this though, you will need
[2:33] an API key and credits. So, you you can
[2:35] add some credits to your account.
[2:38] So, you can top up your balance
[2:41] and then you can get an API key up here,
[2:44] which will allow you to access all of
[2:46] these models through the pie coding
[2:48] agent. I'll just show you how to set
[2:49] that up quickly. Okay, so the way you
[2:51] set it up with open router, you need to
[2:54] export
[2:55] open router_
[3:00] API_key
[3:02] equals whatever the value of your API
[3:04] key is and then you can start up the
[3:06] agent.
[3:08] If you do this, then it will be
[3:09] registered and you'll be able to use any
[3:11] of the um
[3:13] open router models. So, if you take a
[3:14] look here, I already have this
[3:15] configured. So, if I type in /model
[3:19] and then if we select open router, you
[3:21] can see here I had I have access to all
[3:23] of these different models. The GLM 5
[3:26] model, quan models, all of the Google
[3:28] open source models. Pretty much
[3:30] everything you can think of, you can get
[3:32] through this single paid subscription.
[3:34] The one thing I would say is this is
[3:36] quite expensive if you're using top tier
[3:38] models. For example, yesterday I burned
[3:40] through about $15 of credits in a in a
[3:42] very short amount of time. So, for me
[3:44] this approach isn't sustainable unless
[3:47] you're using a much cheaper model. So,
[3:49] let's take a quick look at a few things
[3:50] you might want to check out. The first
[3:53] one is the /command. So, if you use a
[3:56] slash, you can get access to all of
[3:58] these different commands you see here.
[4:00] The settings menu allows you to
[4:02] customize various things about the
[4:04] agent. For example, hiding thinking
[4:08] traces,
[4:10] the theme and the thinking level as
[4:12] well. So, if you're using a thinking
[4:14] model, you can configure this here. The
[4:16] other thing to take a look at is the hot
[4:17] keys function.
[4:19] So, this just shows you all of the
[4:21] keyboard shortcuts essentially that you
[4:23] can use. There's a couple that I use all
[4:25] the time. The first one is shift and
[4:27] tab, which will cycle the thinking
[4:28] levels.
[4:29] But, you can also use this one down
[4:31] here, which is to execute a bash
[4:33] command. You also get this through
[4:35] Claude code, but it's very very useful.
[4:38] Essentially, what it allows you to do is
[4:40] run any arbitrary bash command. So, the
[4:42] way I would use this typically is to
[4:43] open my text editor within the current
[4:46] directory. Much easier than having to
[4:48] drop out of the agent and then come back
[4:49] in again. Okay, so what's interesting
[4:51] about this coding agent in particular is
[4:53] it has a very very minimal set of basic
[4:55] tools by default. So, we have a read
[4:59] tool, a bash tool, an edit tool and a
[5:02] write tool. So, the thinking behind this
[5:05] is that most of the things you want to
[5:06] do
[5:07] for a coding agent, you can basically do
[5:09] via bash because this is able to execute
[5:12] pretty much anything you can think of.
[5:14] Agents are well trained on using bash
[5:17] using reinforcement learning and so they
[5:19] know how to use this tool very well.
[5:21] That's the general principle behind this
[5:23] and so it's a very very minimal tool set
[5:25] here. So, one thing to be aware of as
[5:27] well with this coding agent, there are
[5:28] no permission prompts. So, there's no uh
[5:31] permission settings. Pie runs with full
[5:33] access by default and the philosophy is
[5:36] that most permissions that you get with
[5:38] a tool like Claude code, people are just
[5:40] mindlessly clicking accept anyway and so
[5:42] there isn't really any point to that.
[5:45] If that makes you uncomfortable, you can
[5:47] actually build in your own permission
[5:49] gate extension if you wanted to. So,
[5:51] another interesting feature of this
[5:53] coding agent is the ability to import
[5:55] and export sessions. So, if you type
[5:58] export, it will export the current
[6:00] session as a HTML file and you can also
[6:02] import one as well. So, that's kind of
[6:04] super useful. There are a couple of
[6:06] interesting things about session
[6:07] management which are worth playing with.
[6:10] I don't use them a lot myself, but I do
[6:12] find them interesting features. The
[6:13] first one is the tree,
[6:15] which shows you your session tree and
[6:18] you can also do another command, which
[6:21] is the fork command, which will allow
[6:24] you to fork your conversation. So, if
[6:26] you've got a long-running conversation
[6:28] and you have a message which sends the
[6:30] agent in the wrong direction, you want
[6:31] to go back and re-correct the agent. You
[6:34] don't want to have to keep prompting it
[6:35] or like go through a long cycle. You can
[6:37] actually just jump back to any other
[6:39] point in your conversation and then fork
[6:42] or branch from that point, which is
[6:43] really useful. So, it's worth mentioning
[6:45] I put together a complete guide for this
[6:47] whole video. So, if you want to check
[6:49] this out, I'll put a link in the
[6:50] description. It's got a load of extra
[6:52] notes that you might want to see. Okay,
[6:54] so let's quickly look at the
[6:55] configuration for this agent. So, all of
[6:57] the settings live in this folder, which
[7:00] is at your home directory/ .pi. And if
[7:03] we take a look inside here, you can see
[7:05] there's an agent directory.
[7:07] This is where you can store your
[7:08] agents.md file. This is a global set of
[7:11] instructions that will be used or read
[7:13] every single time the agent starts up.
[7:17] And this is a way of customizing the
[7:19] agent's behavior.
[7:21] And you can see here I've got some
[7:22] instructions.
[7:24] Make the smallest change that saves the
[7:25] task, etc. This is just an example here
[7:27] for your reference.
[7:29] And then also you can see a bunch of
[7:31] other things in here. This is where the
[7:32] settings are stored as JSON file
[7:35] and you can also store your extensions
[7:38] and sessions and your skills here as
[7:41] well. So, this is the directory where
[7:43] everything is stored.
[7:45] For the agents.md file, you can also
[7:47] place it directly in your project repo
[7:50] and it will be found. But, if you want a
[7:52] global agents.md, this is the location
[7:54] where you'd put it. So, I mentioned
[7:56] earlier that you can use the open router
[7:58] model as well, but you can also use
[8:00] things like Ollama as well. If you want
[8:02] local models, you can use those with pie
[8:05] easily. So, that's another option if you
[8:08] want to use local AI.
[8:10] The interesting thing about pie in
[8:12] particular is you can customize the
[8:13] system prompt. So, it has a very very
[8:15] small system prompt out of the box. If
[8:18] you contrast this with something like
[8:19] Claude code, which has a pretty massive
[8:21] system prompt, this is very very
[8:23] minimal. So, it's just saying that
[8:25] you're a coding agent, you help users by
[8:28] reading files, executing commands and
[8:30] editing etc.
[8:32] So, what's really interesting is you can
[8:34] append extra instructions to this system
[8:37] prompt. So, you can create a full a file
[8:40] in this directory
[8:42] called append system and this will allow
[8:44] you to add extra instructions to the
[8:46] system prompt. So, the system prompt
[8:49] allows you to basically customize the
[8:51] behavior of the agent.
[8:53] You can also completely replace it
[8:56] by creating a system.md file as well. I
[8:59] really like this idea because I've
[9:00] always wanted the ability to customize
[9:02] agents. To give you a tangible example
[9:04] of where you might use this, if you want
[9:06] to use this agent for things that aren't
[9:08] coding, you might want a system prompt
[9:10] that doesn't start with you are a coding
[9:12] assistant. So, you might want to
[9:14] specialize this agent to do other types
[9:16] of work, which is totally possible and
[9:19] that's where you might want to have a
[9:20] different system prompt. Okay, so let's
[9:22] move on to extensions, which are
[9:24] probably the most interesting feature of
[9:26] this entire agent. So, unlike every
[9:29] other coding agent out there, pie lets
[9:30] you extend and customize it. So,
[9:33] extensions are just type script files
[9:35] that extend the agent's default
[9:37] behavior. All you need to do is put
[9:39] these files in this location here. So,
[9:42] .pi agent extensions.
[9:46] And then these will get auto loaded. So,
[9:47] these are really powerful. So, you can
[9:49] obviously change things such as
[9:51] customizing the UI,
[9:53] but you can also build in custom tooling
[9:55] or custom workflows as well. So, if you
[9:58] have a particular workflow or unique set
[10:02] of requirements, you can now actually go
[10:04] and build an extension for yourself,
[10:06] which is really, really interesting. So,
[10:08] we're going to build a couple of
[10:09] extensions together now.
[10:11] Okay, so the first thing we're going to
[10:12] do is build a really simple UI
[10:14] extension. Then, we're going to move on
[10:16] to something more complicated. So, I
[10:18] have a prompt here and it just says
[10:21] essentially, this is going to build an
[10:22] extension for Pi that shows the Git
[10:24] status in the UI. This is the kind of
[10:26] thing you have in your terminal that
[10:28] might be useful. Kind of just showing
[10:29] that you can customize the UI. So, let's
[10:31] go ahead and boot up Pi.
[10:34] And then, what we're going to do is go
[10:35] and read that file.
[10:38] So, we're going to say read the file at
[10:42] at extension.
[10:44] We're going to read this prompt here
[10:47] and implement
[10:50] the extension.
[10:52] So, what I recommend is to use the agent
[10:55] itself to build your extensions. It
[10:57] already has access to its own source
[10:59] code. So, what's really interesting
[11:01] about this agent, it can read its own
[11:02] documentation. This is a really
[11:04] interesting meta thing. So, it knows how
[11:07] to write extensions for itself. It's
[11:09] like extendable.
[11:11] And so, I recommend just using the agent
[11:13] to build any extensions you want. One
[11:15] interesting thing to notice is what as
[11:17] it's building this extension, it's worth
[11:18] noting that this here is also a custom
[11:21] extension I built to mimic the Claude
[11:23] code behavior. So, it just goes to show
[11:25] you how much of this can actually be
[11:26] customized. All right, so we built out
[11:28] the extension, but because I'm I'm in an
[11:30] extensions repo, I don't think it's put
[11:32] it in the right place. So, can you
[11:34] install that in the correct location for
[11:37] me? All right, so you can now see it's
[11:39] installed it in the correct directory.
[11:40] So, this extension now lives in the .pi
[11:43] folder agent extensions in the right
[11:45] place. And we should be able to just hot
[11:48] reload. So, if you type {slash} reload,
[11:50] then you can actually just reload the
[11:53] the feature and then you can already see
[11:54] that we have this extension down the
[11:56] bottom here now. So, you can see we have
[11:58] three unstaged changes and then six
[12:01] untracked changes. So, this shows you
[12:03] not only what branch you're on, but also
[12:05] the number of unstaged changes. So, this
[12:08] is a simple example, but it just shows
[12:09] you how much can be customized here
[12:12] really, really easily. Use the agent to
[12:14] write extensions for you and it's very
[12:17] easy to customize. Okay, so what we're
[12:18] going to do now is build a more
[12:20] elaborate extension. And so, this is one
[12:23] that I've been thinking about myself for
[12:24] a long time. So, I have a bunch of
[12:26] extensions that I've written, but the
[12:28] one we're going to take a look at now is
[12:29] the context workflow extension. And so,
[12:32] the idea here is that we can customize
[12:35] the workflow within the agent. So, the
[12:38] thing that I find frustrating with
[12:39] coding agents in general is that you
[12:41] often have them write code, but then you
[12:43] also follow the same process every time.
[12:46] So, they write code, you ask the agent
[12:49] to review the code, it will find a bunch
[12:51] of errors, then you ask it to fix those
[12:53] errors, then you run the tests, and then
[12:55] you fix the failures. So, you go through
[12:56] the same cycle over and over again. And
[12:59] so, this is the correct development
[13:01] cycle. You never want to take the first
[13:04] output, you always want to iterate.
[13:06] And so, what what I wanted to do is
[13:08] essentially encode that workflow
[13:10] into an extension. So, I'm going to show
[13:12] you how that works now. Okay, so let's
[13:14] take a look at a much more complex,
[13:16] non-trivial extension. A lot of the
[13:18] examples you see will be trivial and
[13:21] they won't make sense because obviously
[13:23] customizing the UI is interesting, but
[13:25] it's not very useful in general. So,
[13:27] we're going to look at a much more
[13:28] powerful extension. So,
[13:31] the extension I have is called workflow.
[13:34] And essentially, what this does is it
[13:36] runs a predefined
[13:38] set of steps, almost like a pipeline.
[13:40] So, we're going to read a specification,
[13:43] we're going to write the code, then
[13:44] we're going to review the code,
[13:47] improve the code based on whatever
[13:49] issues we find, and then we're going to
[13:51] run some tests. So, you can encode your
[13:53] entire workflow without having to be in
[13:55] the loop with the agent. This is a
[13:57] really powerful extension. Okay, so in
[13:59] order to run this extension, we're going
[14:01] to actually build an API. So, we have a
[14:04] specification already created. So, I'm
[14:06] just going to show you what that looks
[14:07] like. All right, so you can see here we
[14:09] have a spec and it's basically
[14:10] describing how to build a simple
[14:13] CRUD-based REST API using Python.
[14:16] Nothing particularly interesting. We've
[14:18] described the technical stack.
[14:20] And then, we have some requirements as
[14:21] well. We have all of the endpoints we
[14:23] want to build. So, this is a very
[14:25] typical spec you might have to build a
[14:28] feature.
[14:29] And so, if we go back to the agent, what
[14:30] we're going to do is do this as a
[14:32] workflow. So, I'm going to kick this off
[14:34] now. And so, the idea here is we're
[14:36] going to go through multiple stages as
[14:38] we implement this feature.
[14:39] So, I'm going to kick off the workflow
[14:41] extension.
[14:42] And you can see here now we're at stage
[14:44] one. And then, you can see down the
[14:45] bottom here we're looking at the
[14:48] different stages or the different steps.
[14:50] And you can see how many steps we've
[14:51] completed. So, you can see we're at the
[14:53] current stage where we're writing the
[14:55] implementation. And then, as we work
[14:57] through the workflow, you'll see this
[14:59] update and you'll see the agent will
[15:01] manage its own context window. You can
[15:03] see here now we're running the tests.
[15:05] This is not a prompt. This is more
[15:08] deterministic. So, this is the first
[15:10] time I figured out that these extensions
[15:13] were really, really powerful. Stuff like
[15:15] this, I think, is incredibly useful.
[15:18] And I can see people doing a lot more
[15:20] with this this kind of thing. Okay, so
[15:22] now we're onto the code review step. I
[15:24] mean, to me this is really exciting
[15:26] because this is something I've always
[15:27] wanted the ability to do.
[15:29] And it's something I've
[15:33] these more complex, multi-step workflows
[15:35] within AI agents. And this was a trivial
[15:39] extension to build. I think it took me
[15:40] maybe 20 minutes to put this together,
[15:42] but it just goes to show the power of
[15:44] extensibility. What's good about the
[15:46] code review step here is we're actually
[15:47] reviewing it with a fresh context
[15:49] window. So, within the extension, what
[15:52] happens is we ask the agent to flush its
[15:54] context or to run this with a separate
[15:56] context window. And so, everything we
[15:58] want to happen when we implement any
[16:01] kind of AI coding workflow, we can
[16:03] implement in deterministic
[16:05] extensions and I think this is such a
[16:07] powerful idea. So, while we're waiting
[16:09] for that to complete, let's go and take
[16:10] a look. You can see here now we've built
[16:11] out the user API. You can see here
[16:14] everything's been built. So, this is a
[16:16] production-ready fast API REST API.
[16:19] And you can see here we've implemented
[16:21] the tests as well. So, this is really
[16:23] nice. Not only have we implemented the
[16:24] code, but we've also followed good
[16:27] standard software engineering best
[16:28] practices around testing as well. So,
[16:31] this is a step beyond just vibe
[16:33] prompting or spec-driven development.
[16:35] We're encoding an entire complex
[16:37] workflow into the agent. Okay, so now
[16:40] we've done the code review. The agent
[16:42] has automatically moved on to fixing the
[16:44] issues. This is so exciting to me as
[16:48] someone who has to manually prompt
[16:49] through this all of the time.
[16:51] This is really exciting to have an agent
[16:54] able to execute an entire workflow and
[16:57] manage state as it moves through all of
[16:59] these steps. All right, so you can see
[17:01] here now that the tests are passing. We
[17:04] are calling the workflow.next. And so,
[17:06] this is a built-in tool where the agent
[17:09] can kind of manage its own state
[17:11] throughout the workflow. So, the agent
[17:13] has completed the step and now it's
[17:15] moving on to the next stage of the
[17:16] workflow. So, now we're at stage six,
[17:19] which is the final verification step.
[17:22] So, we're now just checking everything
[17:23] works correctly. We're running the test
[17:25] again
[17:26] based on fixing an issue and now we've
[17:28] gone to run the test again. Everything
[17:31] looks like it's passing.
[17:33] So, it looks like we should be done
[17:34] after six iterations. We went through
[17:37] review, we fixed the issues, we
[17:39] retested, and then we finally verified
[17:41] that everything was correct.
[17:43] And you can see here now we've fixed the
[17:45] issues. We've added extra coverage. So,
[17:48] what's really clever here is that the
[17:49] agent not only wrote the code, it then
[17:52] reviewed the code and found issues, and
[17:54] then it added additional
[17:56] and then finally, it verified that
[17:58] everything was working. So, I think this
[17:59] is a good example of how complex
[18:02] these extensions can get. Okay, so let's
[18:04] move on to the next concept, which is
[18:06] skills. So, most coding agents support
[18:09] the notion of skills. They're on-demand
[18:11] capabilities. They're basically just
[18:13] prompts with optional code or scripts
[18:16] that can be run. Essentially, it's just
[18:18] a set of standard operating procedures
[18:20] for an agent to do a particular task.
[18:22] You can have skills in the following
[18:24] directory. You can put them in the .pi
[18:26] agent skills directory.
[18:28] This is one thing you can do. You can
[18:30] also have them in your local project as
[18:34] well if you want project local skills.
[18:36] So, kind of just what you'd expect.
[18:40] And the way you invoke the skill is to
[18:41] type {slash} skill and then the name.
[18:43] So, this is slightly more explicit than
[18:46] you might be used to. One thing I would
[18:48] quickly show you on skills
[18:50] that I'm using myself is this idea of
[18:55] having an external repo where you keep
[18:56] your skills. So, rather than keep them
[18:59] hidden in sort of
[19:00] dot files or dot folders on your file
[19:03] system,
[19:04] I have a repo with the skills that I use
[19:06] for my daily development tasks. I can
[19:08] easily swap this out. And the reason I
[19:10] like this is because I don't like having
[19:12] skills scattered in multiple different
[19:14] directories all over the place. I found
[19:16] with Claude code, everything was
[19:18] becoming really, really messy.
[19:20] And so, what I've done here is I just
[19:21] have these skills that I actually use
[19:23] all the time and I've just referenced
[19:25] the location of those skills here in the
[19:26] config. And I find this to be really
[19:30] useful. So, if I type up type in Pi,
[19:32] let's start the agent.
[19:34] And so, if you want to execute a skill,
[19:36] you type {slash} skill. And you can see
[19:38] here the only skills I have are the ones
[19:41] that I've put in that particular
[19:42] directory. So, I've got a couple of
[19:44] skills here for building a task,
[19:46] checking code coverage, debugging,
[19:48] planning, refactoring, writing a spec,
[19:51] etc. So, let me just quickly show you
[19:53] how a skills work. So, you in order to
[19:55] invoke a skill, you can type {slash}
[19:57] skill and then the name of the skill.
[20:00] All right, so we're going to build a
[20:01] simple to-do app. So, I'm going to do
[20:02] the spec skill simple to-do app.
[20:07] This is a skill that I created myself.
[20:09] This is my general development workflow.
[20:11] So, the idea here is we create a spec,
[20:13] which describes the requirements of what
[20:16] we want, and also the technical
[20:18] implementation of how we're going to
[20:19] build it as well.
[20:22] So, build a small web to-do app for one
[20:24] user. Make sure that we can edit,
[20:27] complete, delete, and add to-dos. Use
[20:30] SQLite as the database. Show only active
[20:33] to-dos by default.
[20:35] Validate that a title is required.
[20:38] Return error messages.
[20:40] And make it so that I can run it locally
[20:43] with one command.
[20:45] All right, so this is just a basic app.
[20:47] We're just going through the cycle of
[20:48] building something using these skills.
[20:50] Okay, so we're writing this spec down to
[20:52] disk. So, let's go ahead and take a look
[20:54] at what it looks like. So, if we go back
[20:56] into VS Code,
[20:59] we should now have a spec
[21:01] somewhere here. So, we've got this
[21:03] simple to-do app, and now we have a
[21:04] spec. So, we've got
[21:06] a description of what we want. So, here
[21:08] are the requirements.
[21:11] And then we've also given it a given a
[21:12] design as well. So, this is the
[21:15] shape of the JSON responses. I'm not
[21:17] going to bother reading this. I'm just
[21:18] going to go ahead and actually build it
[21:19] or implement it. All right, so now that
[21:21] we have the spec at this location, what
[21:25] I'm going to do is go ahead and break
[21:26] this down into tasks. So, I'm going to
[21:28] do skill
[21:30] plan.
[21:31] And then I'm just going to pass in the
[21:32] spec. So, we're going to break this down
[21:34] into a number of simple steps or tasks
[21:37] that the agent can execute. We're going
[21:39] to do phase one, phase two. So, phase
[21:41] one, building the core infrastructure
[21:43] and the setup. And then we're going to
[21:44] go through each of those steps and build
[21:47] it one by one. Okay, so now we have a
[21:48] plan. The agent has broken this down
[21:50] into a number of phases. Obviously, this
[21:52] is such a simple app, it probably
[21:54] doesn't make sense to do this. We could
[21:56] probably just one-shot it. But, it just
[21:58] shows you the general pattern here. So,
[22:00] we can see phase one, we have the
[22:03] exceptions criteria, we bootstrap the
[22:05] service, and then we have a verification
[22:07] command to make sure it all works.
[22:10] And then in phase two, we create the
[22:12] to-do flow,
[22:14] and so on and so on. So, let's just go
[22:16] ahead and build this out.
[22:19] So, what I would typically do here is
[22:20] work through these one by one and then
[22:23] review and test each stage. But, we're
[22:24] just going to go straight through it and
[22:25] say, "Can you go ahead and implement
[22:32] all of the phases and tasks and build it
[22:36] out?"
[22:39] So, as I said, normally I would go
[22:40] through
[22:42] incrementally do this, but we're just
[22:43] going to go through and see what we can
[22:45] come up with and just build something
[22:46] for real.
[22:47] So, if you're coming from Claude Code, I
[22:49] put together a little bit of a guide to
[22:50] kind of help you mentally map or make
[22:52] the transition. So, the Claude Code will
[22:55] have a claude.md,
[22:57] and the Pi equivalent will be an
[22:59] agents.md.
[23:01] Um Claude obviously has permissions
[23:03] modes, but Pi doesn't by default. Claude
[23:06] supports MCP servers, but Pi is
[23:08] obviously minimalist and it doesn't
[23:10] support these out of the box. You can
[23:12] implement MCP via an extension if you
[23:14] want, but the general philosophy behind
[23:16] Pi is to keep things simple. And so,
[23:19] you'll probably be using
[23:21] a command-line tool instead of MCP.
[23:24] And you can see here the compaction
[23:26] command is the same. Claude supports
[23:29] sub-agents, but the Pi agent does not.
[23:32] And you can see here, rather than hooks,
[23:34] we have extensions.
[23:36] We don't have a to-do task list
[23:38] tracking. We keep things really simple.
[23:40] So, everything in Pi is much simpler and
[23:44] easier.
[23:46] And you gain
[23:48] quite a lot in terms of the context
[23:50] window. So, Claude's system prompt is
[23:51] around 14,000 tokens. Pi's system prompt
[23:54] is obviously very small, and you can
[23:56] customize it. You can also switch
[23:58] between any models using Pi as well. So,
[24:01] you do gain a lot from this coding
[24:03] agent. The only downside, as I've said
[24:06] before, is probably the lack of ability
[24:08] to have the Anthropic subscription. But,
[24:11] if you're not dependent on that, this is
[24:12] a great agent. And just some final notes
[24:15] to kind of close this out. So, there are
[24:17] some advanced commands that you should
[24:18] know about. The first one is this kind
[24:21] of one-shot or uh
[24:23] agent terminal-based execution. Claude
[24:26] Code also supports this as well. So, you
[24:27] can just run it as a single command. So,
[24:31] you can just run this in your terminal.
[24:32] You don't have to start the interactive
[24:34] mode. There's also a JSON mode if you
[24:36] want structured output for the events.
[24:39] And there's also an SDK as well. So, if
[24:42] you wanted to embed this into your own
[24:44] apps, I don't think this is something I
[24:46] would use myself, and neither is the RPC
[24:48] mode. But, it's useful to be aware that
[24:51] these things do exist.
[24:53] Okay, so you can see here now we've
[24:54] completed our to-do list or our to-do
[24:57] server. So, we can actually go ahead and
[24:58] run this. Um can you can you run the
[25:02] app?
[25:03] So, let's go ahead and run the app.
[25:04] Maybe run some tests. Okay, so let's
[25:06] have a look at this app. It looks pretty
[25:08] simple. So, we can add in our tasks,
[25:10] task one, task two. We can edit them.
[25:14] Uh we can mark them as complete, and
[25:16] then we can also delete them as well.
[25:17] So, pretty basic stuff, but this is a
[25:20] finished to-do app. Okay, so now that
[25:22] we've built out our to-do app, we can
[25:23] also run some tasks as well. So, we can
[25:25] run the other skill, which would be to
[25:28] let's take a look at review. So, let's
[25:31] review the code changes and see what's
[25:35] ready for improvement. Okay, so code
[25:38] review is complete. It's found a bunch
[25:39] of issues. What I really like about the
[25:42] skills in general here
[25:45] is that you can have this custom
[25:47] directory. I really like being able to
[25:48] keep everything here in one place, and
[25:51] keeping my skills really minimal. So,
[25:52] all the only skills I have in this repo
[25:54] are related to coding, test-driven
[25:57] development, code review, and stuff like
[25:59] that. So, I really like this uh ability
[26:01] to have a custom directory for your
[26:02] skills. You want to use extensions when
[26:04] you need to run code, things like
[26:07] intercepting tool calls, adding stuff to
[26:09] the UI, registering tools. And you want
[26:11] to use skills when you need to inject
[26:13] instructions for specific types of task.
[26:16] So, for example, a great use of a skill
[26:18] would be to have a code review skill or
[26:21] a refactoring skill, for example. So, if
[26:24] you do want to check out the source code
[26:25] for this agent, this is the repo here.
[26:27] So, it's Pi mono packages coding agent.
[26:30] The documentation is extremely good for
[26:33] this agent. And so, if you ever want to
[26:36] understand how things work, definitely
[26:37] check out the docs. They were written
[26:39] incredibly well. And agents can read
[26:42] this documentation. So, if you do ever
[26:45] get stuck with this agent, just ask the
[26:47] agent to review and read its own
[26:48] documentation, and it will be able to
[26:51] help you. If you're interested in any of
[26:53] the extensions I showed, I have a
[26:55] context workflow extension here. And
[26:58] then I also have this funny status.
[27:01] Essentially, it just puts these funny
[27:02] messages at the bottom of your um
[27:04] prompts, which is kind
[27:05] kind of a bit like Claude Code. So, if
[27:07] you want to check those out, I'll link
[27:08] those as well in the description. So, my
[27:10] honest take, I like this coding agent a
[27:12] lot. I would use it in addition to
[27:14] Claude Code, but I wouldn't use it as a
[27:16] full replacement. And the reason is I
[27:19] use the Anthropic models, and I can't
[27:20] bring my subscription to this coding
[27:23] agent. That's the biggest blocker for
[27:24] me. But, if I wasn't using Anthropic
[27:26] models, this is probably the coding
[27:28] agent I would use day-to-day. I like the
[27:29] minimalism. I like the fact you can
[27:32] customize everything. I think that's
[27:33] really powerful. It's a great tool.
[27:36] Definitely something you should check
[27:37] out. If you enjoyed the video, please
[27:39] remember to like and subscribe. Please
[27:41] let me know in the comments if you've
[27:42] got any questions or if you've got any
[27:44] thoughts, if I've missed anything, etc.
[27:46] If you want to go deeper on any of these
[27:47] topics, I run an AI engineering
[27:49] community. I'll put a link in the
[27:50] description below. And I also run an AI
[27:52] consultancy as well. So, if you want to
[27:54] talk about these topics, I'll also have
[27:56] a link there as well. So, thank you for
[27:57] watching, and I'll see you in the next
[27:59] one. Take care.
