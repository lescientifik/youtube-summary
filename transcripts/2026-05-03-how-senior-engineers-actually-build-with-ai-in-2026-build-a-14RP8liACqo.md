---
description: Transcription brute de la vidéo YouTube "How Senior Engineers Actually Build With AI in 2026 | Build a Full Stack Systems Architecture App".
video_id: 14RP8liACqo
url: https://youtu.be/14RP8liACqo?is=yxAQ9eRbfddp4_la
title: 'How Senior Engineers Actually Build With AI in 2026 | Build a Full Stack Systems Architecture App'
author: 'JavaScript Mastery'
language: en
auto_generated: true
duration: 3:58:12
fetched_on: 2026-05-03
---

# How Senior Engineers Actually Build With AI in 2026 | Build a Full Stack Systems Architecture App

**Chaîne :** JavaScript Mastery  
**URL :** https://youtu.be/14RP8liACqo?is=yxAQ9eRbfddp4_la  
**Durée :** 3:58:12

## Transcription

[0:00] It's 2026 and most of the senior
[0:02] engineers I know aren't really writing
[0:05] code anymore. They designed the systems
[0:07] and let AI handle the implementation.
[0:09] And the gap between developers who can
[0:11] do that and developers who can't is
[0:14] dividing the industry right now. This
[0:16] app is what that looks like when you do
[0:18] it well. Realtime multiplayer SAS AI
[0:21] agents running in the background, full
[0:23] production code, and I didn't write a
[0:26] single line of it. An agent built the
[0:28] whole thing. And by the end of this
[0:30] video, you'll have built it too. The
[0:33] same app, the same stack, the same way I
[0:36] did. And here's what makes this
[0:38] different from other AI build tutorials.
[0:40] I built this app using the exact
[0:42] methodology the app itself is designed
[0:45] to teach. Specs first architecture
[0:48] defined every feature planned before we
[0:51] start building. I've been doing this
[0:53] architecture work by hand before every
[0:55] serious project for years. And at some
[0:58] point it hit me. I'm a developer. Why am
[1:01] I doing all of this manually when I
[1:03] could build the tool that does it with
[1:05] me? So I did. This is Ghost AI, a real
[1:09] time collaborative workspace where you
[1:12] describe a system in plain English and
[1:14] an AI agent maps it onto a shared canvas
[1:18] live. Your team edits the design
[1:20] together and when it's ready, the app
[1:23] generates a complete technical
[1:25] specification you can build from. Now,
[1:27] if you've tried building anything
[1:29] serious like this with AI, you already
[1:31] know the wall. The first few hours feel
[1:34] incredible, and then a week later, the
[1:37] agent has forgotten every decision
[1:38] you've made. One new feature breaks
[1:41] three others, and the codebase you were
[1:43] excited about just starts fighting you.
[1:46] That's not an AI problem. It's an
[1:48] architecture problem. And it's the same
[1:50] wall all of you are hitting in your
[1:52] careers where the senior dev advice
[1:55] online sounds great as long as you're
[1:57] already senior. The developers who win
[2:00] in this market aren't avoiding AI and
[2:03] they are not handing everything over to
[2:05] it either. They're learning to think
[2:07] like senior engineers and then using AI
[2:11] to build at the speed of one. And that's
[2:13] what this video teaches. By the end,
[2:16] you'll know how to design a system
[2:18] before writing any code, how to use the
[2:21] sixfile context system I write before
[2:24] every project, and how a senior
[2:26] engineers actually thinks when working
[2:29] with AI. Oh, and that sixfile context
[2:31] system I just mentioned, I've packaged
[2:33] it into a free guide you can grab and
[2:36] use on any of your upcoming projects,
[2:38] not just this one. The link is down in
[2:39] the description. Next, the stack is
[2:42] Nex.js, JS React 19 live blocks for
[2:46] real-time collaboration with agents
[2:48] trigger dev for background work with AI
[2:50] agents clerk for o and user management
[2:54] prisma and posgress for data versel blob
[2:57] for storage all production grade and
[3:00] deployed by the end of the video. So,
[3:03] one person with the right system can now
[3:06] build what used to take a team. And by
[3:09] the end of the next few hours, that
[3:11] person is you. So, let's build it.
[3:17] Before we open up a single tool, I want
[3:20] to spend the next 10 minutes on the part
[3:22] of the video that I think is most
[3:24] important and that decides whether what
[3:28] you're building ships or falls apart in
[3:30] the third week. There's going to be no
[3:32] syntax and no code in this section.
[3:35] Rather, what I'm teaching you is the way
[3:37] that I think before I write a single
[3:40] prompt and the way I plan a build before
[3:43] I touch the agent and the system that I
[3:46] use to keep AI from drifting halfway
[3:48] through a project so that by the end
[3:51] you'll know the conversations to have
[3:53] before you build, the six file context
[3:56] system that turns an AI agent from a
[3:59] guesser into a developer who already
[4:01] knows your codebase and how to break any
[4:04] project into units the agent can ship
[4:07] cleanly one at a time. So, if you've
[4:10] been frustrated by AI breaking your
[4:12] code, then this is the video that fixes
[4:14] it. The intro touched on something I
[4:17] want to sit with for a minute. You heard
[4:19] me say senior engineers a lot. And if
[4:22] you're early in your career, that
[4:24] framing probably hit a nerve. So, let me
[4:27] be direct about what I mean. The job
[4:30] market for developers right now is
[4:32] harder than it was two years ago. Some
[4:35] entry-level work has been automated.
[4:38] Clients who used to hire freelancers for
[4:41] straightforward projects are now doing
[4:43] it themselves. And a lot of people who
[4:45] learn to prompt without learning how to
[4:47] think are now flooding the market. So if
[4:50] you're worried about that, you're not
[4:53] wrong to be worried. But the developers
[4:55] getting squeezed aren't the ones who
[4:57] learned deeply. They're the ones who
[5:00] learned just enough to execute without
[5:03] understanding the system behind it. That
[5:05] was always a fragile place to be. And AI
[5:09] just made that fragility visible faster.
[5:12] So the way through is to learn the kind
[5:15] of thinking that AI cannot replace the
[5:18] architectural thinking, the systems
[5:20] level judgment and then use AI to build
[5:23] at the speed of someone twice your
[5:26] experience. The clearer your
[5:28] understanding of what you're building,
[5:30] the better the AI output. Which means
[5:32] that learning properly isn't a waste of
[5:35] time in the AI era. It's the best
[5:37] investment that makes everything else
[5:40] possible. So when I say things like
[5:43] think like a senior engineer in this
[5:45] video, I don't mean you need 10 years of
[5:48] experience to apply this. These are
[5:50] learnable habits and you can start
[5:52] building them today on this project. And
[5:55] here's something most developers outside
[5:57] of big tech don't really know. At
[6:00] Google, Amazon and Netflix, before any
[6:03] serious project starts, engineers spend
[6:06] weeks writing documents and sometimes
[6:09] months. Design docs, one-pages, RFC's,
[6:14] the format changes by company, but the
[6:16] principle is the same. Figure out what
[6:19] you're building before you build it. And
[6:22] senior engineers at these companies
[6:24] sometimes go months without writing
[6:26] production code. They're designing
[6:28] systems, making architectural decisions,
[6:31] reviewing what other engineers ship. So
[6:34] software engineering has never really
[6:36] been about typing the most lines per
[6:38] day. It's always been about thinking
[6:40] clearly about what should exist before
[6:43] you build it. And AI didn't invent that
[6:47] discipline. It just made it the most
[6:49] important skill in the room. And that's
[6:51] the whole foundation for the specdriven
[6:53] agentic development course that I've
[6:55] been developing for a long time now. So
[6:58] if you want to stay up to date on how
[7:00] that's going and receive an occasional
[7:01] email where I share my thoughts at the
[7:04] current state of the industry, I'll
[7:05] leave the link down below so you can
[7:07] subscribe for the newsletter. But let me
[7:09] immediately make it concrete in this
[7:10] video. Here are two different prompts
[7:13] that two different developers might
[7:15] write to build the same feature. The
[7:18] first one says, "Build me a SAS app with
[7:21] authentication and a real-time canvas."
[7:24] And the second one says, "I'm adding a
[7:26] livelocks room provider to the workspace
[7:28] route. O is already handled by clerk
[7:31] middleware. The canvas uses react flow.
[7:35] Room tokens should be issued only after
[7:38] verifying project membership. Wire the
[7:41] provider into the existing workspace
[7:43] layout without touching the sidebar or
[7:45] navbar." Both developers want roughly
[7:48] the same thing, but the second prompt
[7:51] reveals a developer who knows their off
[7:54] layer, understands their component
[7:56] boundaries, and knows what should and
[7:58] shouldn't be touched. They've thought
[8:00] about the system, so they're
[8:02] communicating decisions and not wishes.
[8:05] So, the AI isn't smarter when it reads
[8:07] the second prompt. The developer is. And
[8:10] that is the difference between vibe
[8:12] coding and what I'm going to teach you
[8:14] which is specd driven development which
[8:17] is also the premise behind that specd
[8:19] driven agentic development course that
[8:21] I'm actively developing. Vibe coding
[8:24] focuses on the outcome. You describe
[8:27] what you want, let the agent run, and
[8:30] react to whatever comes out. For a
[8:33] weekend prototype, that's fine, but for
[8:36] anything you're going to maintain, it
[8:38] just collapses. New features break the
[8:41] old ones. The codebase starts
[8:43] contradicting itself and you spend more
[8:45] time untangling AI mistakes than
[8:48] actually building. Specdriven keeps the
[8:51] thinking with you and gives the agent a
[8:54] system to execute against. You stay the
[8:57] architect and the agent becomes the
[8:59] implementation engine. So how do you
[9:02] actually build that system? Because
[9:04] that's the part that nobody really
[9:05] teaches. It starts before you open up
[9:08] any AI coding tool with a conversation.
[9:11] When I get an idea for something I want
[9:13] to build, I open up a planning AI, Chad,
[9:16] GPT, Claude or Gemini, whichever is on
[9:19] hand, and I talk through it. What does
[9:21] this thing actually do? Who uses it?
[9:23] What are the core flows? Where are the
[9:25] complex patterns? And what could go
[9:27] wrong? I push back on the answers and
[9:30] let AI pressure test my thinking until
[9:33] the system becomes clear in my head.
[9:36] This conversation is the work. It's what
[9:38] senior engineers do before they build.
[9:41] Except they usually do it in their head
[9:43] or on a whiteboard, but doing it with AI
[9:46] externalizes it and makes it faster.
[9:49] When the system is clear, you write it
[9:51] down. And that's where the six file
[9:53] context system comes from. Not from
[9:55] sitting at a blank page trying to write
[9:57] documentation, but from taking the
[9:59] output of the architectural conversation
[10:02] and organizing it into documents that
[10:04] travel with the project for its entire
[10:07] life. For Ghost AI, I organized
[10:10] everything into one folder called
[10:12] context, six files. And what matters is
[10:15] that before your AI agent writes
[10:17] anything, it already knows what you're
[10:19] building, how it fits together, what the
[10:21] rules are, and where things stand right
[10:24] now. That's what you're going to learn
[10:25] about in this video. But very quickly,
[10:28] here's what each one of them does at a
[10:30] glance. The project overview covers what
[10:34] the product is, who is it for, the core
[10:37] flows, and what's deliberately out of
[10:39] scope. The architecture file defines the
[10:42] text stack, the boundaries between
[10:44] layers, and the invariance the codebase
[10:47] must never break. The code standards
[10:50] keeps the agent consistent across every
[10:52] unit of the build with shared TypeScript
[10:55] and Nex.js conventions. The AI workflow
[10:58] rules keep the agent disciplined,
[11:00] defining how to scope work and what to
[11:02] do when something needs a decision. The
[11:05] UI context holds the design tokens and
[11:08] component conventions so the UI stays
[11:11] coherent across every page the agent
[11:13] ships. And the progress tracker, which
[11:16] is the one most developers skip and most
[11:18] need, holds the current phase, what's in
[11:21] progress, what's complete, and the
[11:24] architectural decisions made along the
[11:26] way. It's the only file that actually
[11:28] updates constantly throughout the build.
[11:30] And it's how the agent picks up exactly
[11:32] where you left off in a single prompt.
[11:34] These six files are what make the
[11:37] difference. An AI agent that drifts and
[11:40] one that executes. And you don't have to
[11:42] build them from scratch for every
[11:44] project. I've put together a free blank
[11:47] template of all six files with
[11:49] step-by-step instructions on how I
[11:51] generate them using AI for whichever
[11:54] project I'm working on. And it's not
[11:56] specific to Ghost AI. It works for any
[11:58] application. Click the link down in the
[12:00] description to get it so you can apply
[12:02] this methodology to your own projects
[12:04] starting today. We'll open up each one
[12:07] of these and I'll walk you through
[12:08] what's actually inside in the next
[12:10] lesson when we set up the project
[12:12] architecture for real. But yeah, once
[12:15] these six files exist, the build runs in
[12:17] units. We're going to break down the
[12:20] project into specific scoped pieces
[12:22] before we start. Not vague phases like
[12:25] build a dashboard, but concrete units
[12:28] small enough to build in a single focus
[12:31] session with clear conditions for what
[12:33] done looks like. That means that
[12:36] together for ghost AI, we'll map out the
[12:38] entire build. Each lesson will have its
[12:41] own spec file. The spec defines the
[12:44] goal, the design decisions, the
[12:46] implementation details, dependencies,
[12:48] and a checklist of what has to be true
[12:51] before the unit is complete. You write
[12:53] the spec in the same way you write the
[12:55] context file through a conversation with
[12:58] a planning AI. Then you give the spec to
[13:01] your coding agent in one prompt. Make
[13:03] sure to read that spec, mark that unit
[13:06] as in progress in the progress tracker,
[13:08] implement it exactly as specified
[13:11] without going beyond scope. The agent
[13:13] will read your spec, read your context
[13:16] file, and build against a defined system
[13:20] instead of guessing. You review it
[13:22] against the checklist and if it passes,
[13:25] you close the unit, push the code, and
[13:28] move to the next spec. If something's
[13:30] off, you write a focused corrective
[13:33] prompt exactly what's wrong, exactly
[13:35] what you expect, fix that specific
[13:37] thing, and move on. That's the entire
[13:40] workflow. The same one I used to build
[13:43] Ghost AI, and the same one you're about
[13:45] to use to build it with me. Oh, and last
[13:48] thing before we begin. These files take
[13:51] time to write. The conversation, the
[13:53] architectural decisions, the unit
[13:55] planning, all of it is real upfront
[13:58] work. And a lot of developers skip it
[14:01] because they want to feel productive
[14:02] immediately. I mean, I've done that as
[14:05] well. So, you open up the agent, type a
[14:08] prompt, and start watching code appear.
[14:11] But that's the trap. The time you save
[14:14] by skipping this is the time you'll lose
[14:17] in week three debugging AI output that's
[14:20] drifted away from anything coherent. So
[14:23] do this work once and you'll do it
[14:25] faster every project after. And finally,
[14:29] it's time to build.
[14:33] Okay, enough talk and let's build. Open
[14:36] up your desktop and create a new folder.
[14:39] call it something like ghost AI and then
[14:43] simply drag and drop it into your
[14:45] favorite code editor. For this video,
[14:47] I'll be using VS Code as we have the
[14:49] file explorer on the left side. We have
[14:51] the code in the middle and then we have
[14:54] the chat window which you can open up by
[14:56] pressing command shiftp and then just
[14:58] search for chat or I think it's just
[15:01] command shift I to open it as well. No
[15:03] matter which agent you're using, is it
[15:05] Copilot, Claude, Codeex or whatever, the
[15:08] interface is more or less the same. This
[15:10] is how it looks like on Codex. And this
[15:13] is just general chat. So this video is
[15:16] completely agentic tool agnostic. The
[15:19] thinking and the specs are what matters.
[15:22] The tool is completely your call. I'll
[15:24] personally be using cloud code as that's
[15:27] what most people are using and what
[15:28] we're using internally within JSM. If
[15:31] you want the budget option, you can go
[15:32] with Codex. There's the Go plan, which
[15:35] is super cheap. The Plus plan, which is
[15:37] also cheap, and I think they're also
[15:39] offering a month for free. And if you're
[15:41] already paying for something like
[15:42] Cursor, Windsurf, or any other AI agent,
[15:46] just use that. I'll make sure you don't
[15:48] spend a lot of tokens, no matter what
[15:49] you're using, and that you'll learn a
[15:51] ton. Okay, so let's get started. We'll
[15:54] start with a fresh Nex.js project. I'll
[15:57] do this manually with no prompts and
[15:59] agents. It's just a single command and
[16:02] it takes a couple of seconds and that'll
[16:04] give us a clean and predictable
[16:06] foundation to build everything else on
[16:07] top of. So simply open up your
[16:09] integrated terminal and run MPX create
[16:13] next app add latest dot which is going
[16:16] to create it in the current repository.
[16:17] It'll ask you whether you want to
[16:19] install the next.js installer. So you
[16:21] can just say why yes and proceed. And I
[16:24] also want you to know that you don't
[16:25] necessarily have to follow along by
[16:27] using Nex.js.
[16:29] Of course, the majority of the context
[16:31] for AI agents we'll be working with is
[16:33] going to be featured around Nex.js. But
[16:36] if you want to build this in Tanstack,
[16:38] Angular, Vue, or anything else, the
[16:40] concepts will still be as valuable. So
[16:43] let's just say Y for now. It's going to
[16:45] ask you whether you would like to use
[16:46] the defaults. So just press enter which
[16:49] is going to install React, TypeScript,
[16:51] ESLint, Tailwind CSS, and the app
[16:54] router. Let's give it a moment until it
[16:56] finishes. Once the installation
[16:58] finishes, we need to clear out the
[17:00] default boiler plate. That's going to be
[17:02] within app and then page. NextJS ships
[17:06] with a lot of placeholder content that
[17:08] honestly we don't really need. Now, you
[17:10] could go ahead and clean it up manually
[17:12] by opening up your globals.css CSS and
[17:16] cleaning everything besides the Tailwind
[17:18] CSS directives, deleting some SVGs and
[17:21] other stuff within the public folder and
[17:23] replacing the page.tsx with a minimal
[17:26] component or we can use this as our
[17:29] first interaction with the coding agent.
[17:33] So go ahead and open up your agent of
[17:35] choice. I'll just press command shift I
[17:38] to open up my chat sessions. And what I
[17:40] love about VS Code is that it's not
[17:43] shying away from the agnostic approach
[17:45] to agents. You can use their agents
[17:48] right here, such as Copilot CLI, or if
[17:52] you head over to extensions and then
[17:54] install an extension like Claude Code,
[17:58] which has like 12 million downloads, or
[18:01] something like Codex, which has 8
[18:03] million downloads, and I installed both.
[18:07] You can actually just navigate over to
[18:08] them by selecting additional views and
[18:11] then choosing the extension you want. Of
[18:14] course, alternatively, you can also just
[18:16] run all of these agents within the CLI
[18:18] by typing claude and you're in. For the
[18:22] longest time, I've been using Claude
[18:23] CLI, but the Claude VS Code extension
[18:26] recently got so much better. And
[18:28] honestly, it's working the same way as
[18:31] the CLI does, but with a bit of a nicer
[18:33] UI and the graphical interface that
[18:35] allows us to use it in an easier way.
[18:37] So, that's what I'll be proceeding with.
[18:39] I'll expand it so we have more space to
[18:41] work with. And you can notice that
[18:43] there's a little microphone button right
[18:44] here. So, you can either tap it or hold
[18:47] the command D key to speak into it. With
[18:50] Codex and other agents, you can either
[18:52] type it manually, or what you can do is
[18:56] use a tool like Whisper Flow, not
[18:58] sponsored by the way, which is what I
[19:00] use to write prompts when I speak with
[19:03] agents. Speaking is just much faster. If
[19:06] you install it, you can just press the
[19:07] command key and start speaking into it.
[19:11] Like, clean up this Nex.js boilerplate,
[19:14] strip globals.css CSS down to just the
[19:17] Tailwind directives. Delete all SVGs in
[19:20] the public folder, but keep the favicon.
[19:23] Remove page.module.css.
[19:26] Replace page.tsx with a minimal
[19:29] component that just renders a center div
[19:32] saying ghost AI. And I can stop it right
[19:36] here. And you can immediately see the
[19:38] output. Cool stuff, right? Go ahead and
[19:40] write something like this. And let's see
[19:42] how well agent handles it. Also, just so
[19:44] we don't have to give it permissions
[19:46] every single time whenever we're doing
[19:48] something. For now, I will say edit
[19:50] manually. Oh, and of course, we have to
[19:52] talk about the actual models which we'll
[19:54] be using. In this case, we're using the
[19:56] default model, which is Opus47 with a
[19:59] million token context, which is amazing,
[20:01] but you're going to hit the limits very
[20:03] soon. Instead, you'll be able to follow
[20:04] along this entire build with using
[20:07] Sonnet 46. It's fast, it's inexpensive,
[20:11] and it sometimes get lost unless you
[20:14] have the context files, which I'll teach
[20:16] you how to build so you guide it in a
[20:18] bit of a better way and make it work
[20:20] much more like Opus does. So, that's
[20:23] what I'm going to select. If you're
[20:24] working with codecs, you can also go
[20:26] ahead and choose any model you'd like,
[20:28] like 54, 53, or anything else. Okay,
[20:31] let's give it a shot. It's going to
[20:33] think for a couple of seconds, read all
[20:35] the necessary files and apply all four
[20:38] changes. Globals, just the import page,
[20:42] minimal centered ghost a component,
[20:44] deleted five SVGs, but kept the favicon.
[20:47] And this file that I tried to trick it
[20:48] with doesn't really exist, so there's
[20:50] nothing to delete. You can see all the
[20:52] changes in the diff right here. And you
[20:54] can also see which files have been
[20:56] modified on the left side. There we go.
[20:58] just simple ghost AI and just the import
[21:02] for Tailwind, which means that these
[21:04] classes right here should work to center
[21:06] the div. Before we run it, let's
[21:07] actually head over to package.json.
[21:10] Make sure that the project name is set
[21:12] to ghost AI and let's run it by running
[21:16] mpm rundev.
[21:18] It'll run it on localhost 3000. So, if
[21:21] you open it up, you should be able to
[21:23] see something that looks like this. This
[21:25] means that our project is initialized.
[21:27] It's cleaned up and now we are ready to
[21:30] move to the part that actually
[21:32] determines just how well everything
[21:34] goes. Setting up our context files and
[21:37] planning the build before the agent
[21:39] writes a single feature. So, let's do
[21:42] that next.
[21:45] Not that long ago, I talked about how
[21:47] senior engineers spend weeks designing
[21:50] systems before anyone writes a line of
[21:53] code. They write design docs. They
[21:56] define boundaries and they make
[21:58] decisions early on so that everything
[22:00] else becomes predictable.
[22:02] So let me show you how we are going to
[22:04] approach that. We're going to create a
[22:07] new folder right here in the root of our
[22:09] application which we're going to call
[22:11] context. Everything inside of it is what
[22:14] your coding agent will read before it
[22:17] does anything. This is how it knows your
[22:19] project and this is how it stays
[22:21] consistent across every session, commit
[22:24] or unit of the build. So you can switch
[22:27] multiple agents and share the context
[22:29] file with another developer so he can
[22:31] continue working with his agent from
[22:33] there. That's the catch. We're going to
[22:35] have a couple of different files within
[22:37] the context folder. Now I don't want you
[22:39] to do a lot of copy pasting. So I'll
[22:42] provide you with the final zipped
[22:43] context folder so we can easily review
[22:46] everything together. So, delete the
[22:48] context folder you just created. In the
[22:50] video kit link down in the description,
[22:52] get the zipped version of the folder.
[22:54] Unzip it and then just drag and drop it
[22:57] in. And here you'll see six, well, seven
[23:00] different files with this agents.mmd.
[23:03] Might seem scary at first, but don't
[23:05] worry as I'll walk you through every
[23:07] single one of these files and show you
[23:09] how you can create them for yourself in
[23:10] the future. Let's start with the project
[23:14] overview. And let me walk you through
[23:16] why it's structured the way it is.
[23:18] Because understanding this is more
[23:20] valuable than just copying the file.
[23:23] Currently, we're looking at the markdown
[23:25] version of the file. But in VS Code, I
[23:28] believe this is done by default. You can
[23:30] also open the preview to the side by
[23:32] pressing command K and then V or just
[23:34] pressing this icon at the top. And then
[23:36] you can close the actual MD and just see
[23:38] the formatted version. I think it's a
[23:40] bit easier to read this way. I typically
[23:42] open up these project overview documents
[23:45] with a one paragraph summary and then a
[23:48] numbered list of goals. This gives the
[23:51] agent the big picture immediately. So
[23:54] when a requirement gets ambiguous 3
[23:56] weeks into the build, and it will, this
[24:00] is where you resolve it. The agent uses
[24:02] this constantly to understand intent
[24:05] when a spec isn't specific enough.
[24:08] Notice the goals are concrete and
[24:10] measurable. Not build a good canvas.
[24:13] Instead, let authenticated users create
[24:16] and manage architecture projects or let
[24:19] AI generate an initial architecture from
[24:21] a natural language prompt. The agent
[24:24] knows exactly what success looks like.
[24:27] And yeah, this is useful for us while we
[24:29] are going through the process of
[24:30] building the app. Just so you know what
[24:32] we are building, just so everybody in
[24:34] the team, in this case me teaching you
[24:36] and you following along and you building
[24:39] it with me, are all on the same page.
[24:42] Ghost AI is a real time collaborative
[24:44] system design workspace. Users describe
[24:47] a system in plain English and an AI
[24:50] agent maps that system onto a shared
[24:52] canvas. Collaborators refine the
[24:54] architecture and the app generates a
[24:56] technical specification document from
[24:58] the resulting graph. Okay, great. We
[25:01] have the overview, we have the goals,
[25:04] and then we have the core user flow. So,
[25:07] let me zoom this in and let's go through
[25:09] this together because this sequence
[25:11] matters. The agent can sometimes lose
[25:14] track of how features connect to each
[25:17] other. By defining a full flow from
[25:20] signin to the spec generation, we make
[25:23] the logical sequence explicit. So the
[25:25] agent won't try to build a spec
[25:27] generation feature on the login page
[25:29] because it knows the user has to create
[25:31] a project and the design architecture
[25:33] first. In the features, we get specific
[25:36] about technologies. And I want to take a
[25:39] second on this because the tools I chose
[25:41] for Ghost AI weren't random. I took a
[25:44] lot of time to choose what actually
[25:46] makes sense. Starting with
[25:48] authentication for user signin, route
[25:50] protection, project creation, ownership,
[25:53] and collaborator access, we're using
[25:55] clerk. Could you have gone and created
[25:57] the full o from scratch? I mean, sure,
[26:00] but it would take you a couple of days
[26:02] up to a couple of weeks to do it
[26:03] properly, even with AI. And when you do
[26:06] it, it's never going to be as secure as
[26:09] something like Clerk. And nowadays, the
[26:11] speed of shipping matters more than
[26:14] anything. If you have a specific product
[26:16] you want to push, you want to get it in
[26:18] front of potential users as soon as
[26:19] possible. And that's why for many of
[26:21] these agentic builds, it's just a
[26:23] no-brainer to plugandplay clerk into it,
[26:26] especially considering just how well
[26:29] clerk works with your agents. You can
[26:31] either just copy the prompt or use clerk
[26:35] skills with whichever agent you're
[26:37] using. That way it'll immediately become
[26:40] a professional developer at using clerk
[26:43] and it'll be able to implement it within
[26:45] any project. And there's also the MCP
[26:48] which is a server that allows AI agents
[26:51] like claude cursor or others to access
[26:54] clerk SDK snippets and implementation
[26:57] patterns and basically implement
[26:59] everything for you. Oh, and not to
[27:01] mention that clerk CLI is also being
[27:04] worked on. You'll just be able to ask
[27:06] your agent to use the Clerk CLI to add O
[27:09] to your app, allowing you to not even
[27:10] have to leave your terminal or copy and
[27:12] paste any API keys. Clerk right now
[27:15] really is the leader in agentic
[27:17] development. And with a completely free
[27:19] pricing of up to 50,000 monthly
[27:23] recurring users, it's a no-brainer for
[27:25] me to build all of my applications with
[27:28] it. So, while we're here, I'll leave the
[27:30] link down in the description. you can
[27:32] click it and then sign up so that we can
[27:34] very soon more easily get started with
[27:36] building. Okay, on top of O the most
[27:38] important part of our application is the
[27:41] collaborative canvas and in this case I
[27:44] wanted to make it real time. So for any
[27:47] kind of canvas, it makes sense to use
[27:49] React Flow. And if you want to make any
[27:51] part of your application live with
[27:53] cursors, so you can see what other
[27:54] people are doing, presence indicators,
[27:57] and node or edge editing. I mean, it
[28:00] just makes sense to use Live Blocks.
[28:01] Livelocks is the leader for anything
[28:04] multiplayer. But not only apps, agents
[28:07] as well. Let me show you what I mean. I
[28:09] mean, this is the app without Live
[28:11] Blocks. And then if you add it, you
[28:14] immediately get live avatars. You can
[28:16] get the AI chat to generate something.
[28:19] And you can also leave comments and
[28:21] track what people are doing within your
[28:23] app, which is super useful for the
[28:24] collaborative canvas we're building. But
[28:26] what's even cooler is interacting
[28:29] directly with AI assistants to do
[28:32] something within our application. I
[28:34] mean, if you try to build all of this
[28:36] from scratch, it would definitely take
[28:37] some time. But with their AI assistance
[28:40] feature, you can just watch an AI do it
[28:42] for you. Oh, and this whole React Flow
[28:44] thing you're seeing, that got released
[28:46] recently, which means that in this
[28:48] video, we're building the latest stuff
[28:50] out there. Oh, and like Clerk and the
[28:52] many other amazing dev tools that are
[28:54] adapting to agentic development,
[28:56] LiveBlocks also offers the agent skills,
[28:59] which you just have to install and your
[29:01] agent will immediately know what it has
[29:03] to do to make the LiveLocks integration
[29:05] work. I'll teach you about all of that
[29:07] as we continue with the build. After the
[29:09] canvas, we have the starter system
[29:11] design, which I decided to have because
[29:14] it's very difficult for people to start
[29:16] with a blank canvas. So, I want to have
[29:18] some kind of a curated library of
[29:20] pre-built system design templates where
[29:23] users can import a starter template into
[29:25] the canvas at any point during editing.
[29:28] but also if the template doesn't do what
[29:30] you want it to do, we're going to allow
[29:31] our users to generate a system design
[29:34] from a prompt with AI. Then that output
[29:37] will be structured as canvas nodes and
[29:40] then we'll write it onto the canvas. And
[29:42] finally, we'll take a look at everything
[29:44] that is on the canvas and we'll convert
[29:46] it into a technical specification in a
[29:48] markdown format and then users will be
[29:50] able to view and download the generated
[29:52] specs. Oh, and an additional thing that
[29:54] I want to teach you is while we're
[29:56] generating stuff with AI, that'll
[29:59] obviously take time as the user will
[30:01] likely provide a long idea of how they
[30:04] want to architect their app and then the
[30:06] AI output is going to take potentially a
[30:08] minute or two and running a more than
[30:11] 60-second AI generation call inside a
[30:14] Nex.js API route will just time out in
[30:16] production. So, that's why I'll also
[30:18] teach you how to use trigger dev. It'll
[30:21] allow us to run background tasks that
[30:23] can run as long as they need to with the
[30:25] retry logic and status tracking built
[30:27] in. The way in which we'll combine live
[30:30] blocks and trigger dev is pretty
[30:32] amazing. So we'll have to be very clear
[30:34] in letting our AI agent understand that
[30:36] it doesn't have to invent a custom
[30:38] websocket implementation when liblocks
[30:41] is already in stack or it won't try to
[30:44] run AI generation inside a request
[30:46] handler when triggered dev is defined as
[30:48] the layer for that work. Naming the
[30:50] tools we're going to use for the project
[30:52] in advance is crucial. Oh, and Trigger
[30:55] allows you to do so much more. Recently,
[30:57] they've been diving deeper into allowing
[30:59] you to build and deploy AI agents, which
[31:01] is something we can explore in an
[31:03] additional video. But in this one, we'll
[31:05] also focus on many of its features,
[31:07] specifically running background tasks
[31:09] and reporting back to the front end. So,
[31:11] while a long task is happening, we can
[31:13] keep the user updated on what's
[31:15] happening behind the scenes and allow
[31:17] the user to continue doing whatever
[31:19] they're doing on the application because
[31:20] we're no longer blocking the front end
[31:22] side while handling a specific task. So
[31:24] I'll leave a special link pointing to
[31:26] trigger as well as live blocks down in
[31:29] the description so you can create your
[31:31] accounts and then we'll be able to
[31:32] immediately dive into the development.
[31:34] Then we have the scope part which
[31:36] contains the in scope and out of scope
[31:38] features and it's maybe the most
[31:41] important section for keeping your build
[31:43] focused. The out of scope section is
[31:45] doing serious work right here. billing
[31:48] and subscription systems, enterprise
[31:50] permissions, version specification
[31:52] history, and so on. This is telling the
[31:55] agent, don't even think about them, but
[31:57] we can add them later on after we build
[32:00] the base of our application. This is
[32:02] great because it keeps every session
[32:03] focused on what we are actually
[32:05] building. And finally, there's success
[32:08] criteria. Here we define what actually
[32:11] matters. These are the benchmarks that
[32:13] your agent and you can verify against
[32:16] after each major feature lands. Not does
[32:19] it look right, but can a signed in user
[32:22] create and open up a project? Can
[32:24] multiple users collaborate? Can the
[32:26] graph be converted into a persistent
[32:28] markdown specification? Very simple yet
[32:31] concrete. So that's our project overview
[32:35] written in a way that makes sense to
[32:37] agents but also other team members
[32:39] working on the project. Next, let's take
[32:41] a look at the AI workflow rules. This
[32:45] file is different from others in a way
[32:47] that it's not about what we're building.
[32:50] It's about how the agent behaves when
[32:52] building it. And the most important rule
[32:54] right here is to work on one feature
[32:57] unit or subsystem at a time. We don't
[33:00] want to combine unrelated system
[33:01] boundaries in a single implementation
[33:03] step. And that single rule prevents most
[33:06] failures that the agents cause.
[33:08] Basically, all of these rules right here
[33:10] tell the agent stay in your lane. Focus
[33:13] on one part of what you're doing and
[33:15] then move on to the next one. After
[33:17] that, we have the code standards. So,
[33:20] you can open up that and let's quickly
[33:23] take a look. This file is what keeps the
[33:26] codebase consistent from our first all
[33:28] the way to the last chapter. Without it,
[33:31] the agent would drift away. like
[33:33] specific patterns that it uses for API
[33:35] routes when implementing feature 5 might
[33:38] look different from feature 16 or maybe
[33:40] it's going to change some things
[33:41] regarding the TypeScript types or how it
[33:43] uses Nex.js GS how it styles things. But
[33:46] here we add that consistency like we
[33:50] tell it make sure to have strict mode
[33:52] enabled and avoid using any or we're
[33:55] telling it to add use client only when
[33:57] the component needs browser
[33:59] interactivity or for styling we're
[34:01] telling it no raw Tailwind color classes
[34:04] reference the tokens through the
[34:06] Tailwind utility names. I think you get
[34:08] the point. We want to stay consistent.
[34:10] Then we have the UI context which as you
[34:13] can guess dives a bit deeper into
[34:16] theming. Like when I was initially
[34:17] coming up with the design for this
[34:19] application, I wanted to have something
[34:21] that is simple yet functional and
[34:23] modern. And I spoke with AI a bit to
[34:26] generate this theme. Dark mode, no light
[34:29] mode. Uh all colors are already defined
[34:32] and we're telling the AI to use these
[34:34] colors. And again, if you're wondering
[34:37] how exactly I created all six of these
[34:40] documents by speaking with different AI
[34:42] agents, that's something that I'll cover
[34:45] in much more detail within the
[34:47] specdriven agentic development course.
[34:49] So, you can join the weight list in the
[34:51] description. But I think you get the
[34:52] idea that I didn't just sit down and
[34:54] handpick every color in the file. I
[34:56] described the aesthetic that I wanted to
[34:58] AI, dark, technical, precise, something
[35:01] that feels like an engineering tool. And
[35:04] then I went back and forth on the pallet
[35:07] um the token names and this is what it
[35:09] came up with. Also some font border
[35:11] radiuses and so on. That's exactly how
[35:14] you should approach your own UI. You
[35:16] don't need to be a designer, but you
[35:18] need to know the feel you're going for
[35:20] and then AI can help you get there. Oh,
[35:23] and while the project overview gave some
[35:26] information about the project, the
[35:28] architecture context will give it the
[35:30] blueprint on how to build it. Here I
[35:32] specified the text stack like every
[35:36] technology that we want to use alongside
[35:37] the role that it has within the
[35:39] application. For O we're using clerk for
[35:41] user identity and route protection. For
[35:43] databases it's going to be prisma and
[35:45] posgress. For canvas it's going to be
[35:48] live blocks and react flow. For
[35:50] real-time collaborative canvas for
[35:52] background tasks it's going to be
[35:54] trigger dev. And for storage we're going
[35:56] to use versel blobs. We also define some
[35:58] system boundaries like where we're going
[36:00] to put the request handlers. Trigger is
[36:03] what we're going to use for the long
[36:04] running background jobs and some other
[36:06] folders that we're going to use. Then we
[36:09] define the storage model where and how
[36:11] we're going to save something. And
[36:13] specifically here I decided to use a
[36:15] hybrid storage model which is another
[36:17] senior level decision. We aren't going
[36:19] to be stuffing massive JSON blobs or
[36:22] three-page markdown files into our
[36:24] database. Instead, we're going to use
[36:26] Postgress only for metadata and Verscell
[36:29] blob for the actual files. And this
[36:32] keeps our database lean. And this is
[36:34] important. We also need to tell it how
[36:36] different tools are working together.
[36:38] Since we're using clerk with liblocks,
[36:40] we need to set a strict rule that
[36:42] project memberships must be verified
[36:45] before a liblocks token is ever issued.
[36:48] This ensures that our ghost AI isn't
[36:50] just collaborative, but secure. And
[36:52] finally, invariance are the rules that
[36:55] the system must never violate. For
[36:57] example, request handlers do not run
[37:00] longived AI works that belongs in
[37:03] background tasks through trigger.dev.
[37:05] Metadata and large artifacts are stored
[37:07] in separate layers. O and ownership are
[37:10] enforced at every mutation boundary.
[37:12] Client components only used when needed,
[37:15] and the canvas schema must remain
[37:17] consistent. Of course, we'll dive much
[37:19] deeper into this when we actually dive
[37:21] into building the application, but I
[37:23] wanted you to have a good idea of what
[37:25] it is that we're building. And finally,
[37:26] there's the progress tracker. This is
[37:29] the only file in the context folder
[37:31] that'll look completely different by the
[37:33] end of this video. Right now, it is
[37:36] completely empty intentionally because
[37:39] it reflects the actual state of the
[37:41] project. And right now, nothing has been
[37:44] built yet. So, as we complete each
[37:46] lesson, we're going to update this file,
[37:48] the current phase, what's in progress,
[37:50] what's complete, and what's coming next.
[37:52] And remember what I said in the
[37:53] beginning about agents having no memory
[37:56] between sessions. This file is the
[37:58] solution to that problem. At the start
[38:00] of every new session, whether that's
[38:02] tomorrow, next week, or 6 months from
[38:05] now, one prompt is all it takes to
[38:07] restore full context. Our agent will
[38:10] read the progress tracker, understand
[38:12] exactly where the project stands, and
[38:14] pick up exactly where you left off, so
[38:17] you don't have to reexplain yourself.
[38:18] Even though it's going to be a small
[38:20] file, it does more work than any other
[38:22] file in the project. Oh, and finally,
[38:24] there's the agents.md file. Within it,
[38:28] we're going to wire everything together.
[38:30] When you install Nex.js,
[38:32] that file was already created for you
[38:34] automatically at the root. This is the
[38:36] entry point file and every major coding
[38:38] agent has one. They just name it
[38:40] differently. Claude calls it claw.md.
[38:43] Cursor windsurf and others use different
[38:46] names, but the idea is always the same.
[38:48] It's the first thing that the agent
[38:49] reads at the start of every session. So,
[38:52] Nex.js has already added the first
[38:54] section for you and it tells the agent
[38:56] that this is a recent version and its
[38:58] training data might be outdated. So,
[39:00] read the installed documentation before
[39:02] writing any code. Good default and we
[39:04] can leave it. But now we can add our own
[39:06] part below it. So copy your agents MD,
[39:10] delete it from the context and instead
[39:12] move it right here. It's not long. So
[39:15] let's see what do we have within it.
[39:17] We're basically instructing the agent to
[39:19] read all six context files in order
[39:22] before implementing anything. And then
[39:24] to update the progress tracker after
[39:27] each change. And you might think, isn't
[39:29] this going to waste context and tokens?
[39:32] Well, I mean, sure, it has to read
[39:33] through the files, but that's not even
[39:35] onetenth of how many tokens you're going
[39:37] to save because there's going to be less
[39:39] back and forth and less mistakes and bug
[39:42] fixing and correcting while you're
[39:44] implementing the features in the first
[39:45] place. So, that's the system and now
[39:48] that you understand it, let's start
[39:50] building with it.
[39:53] Now that the context files are ready,
[39:55] before we build a single feature,
[39:57] there's one more thing we need to set
[39:59] up. And skipping this one is the most
[40:01] common mistake I see in AI assisted
[40:04] projects. And that is the globals.css
[40:08] file. This one right here. We've defined
[40:11] all of our color tokens within our UI
[40:14] context right here. But if we don't
[40:16] translate those tokens into actual CSS
[40:18] custom properties within the globals.css
[40:21] CSS file. Well, it'll just write the
[40:23] inline colors. So, instead of maybe
[40:25] saying something like text faint, it'll
[40:27] just write #505 060. And the moment you
[40:32] want to change it, you have to change it
[40:33] across all places. So, let's set it up
[40:36] correctly. And this is also the first
[40:38] real demonstration of the specd driven
[40:40] workflow in action. So, let's do it
[40:42] properly. Create a new folder inside of
[40:45] the context folder and call it feature
[40:49] specs like this. And then inside of it,
[40:52] create the first spec file 01
[40:57] design system.
[41:00] And then within it, we want to tell it
[41:02] something like read the agents file
[41:04] before starting. Then we need to tell it
[41:07] what we're doing here, like adding the
[41:09] design system and UI components. Then we
[41:13] are telling it to install and configure
[41:15] chat CN UI. And then we wanted to add
[41:19] the following components. I figured
[41:22] we're going to use these across the rest
[41:24] of the application. We never wanted to
[41:25] modify these files after the
[41:27] installation. So we can specify that we
[41:31] can also ask it to install lucid react
[41:33] for icons and create a lib utils.ts ts
[41:38] with a reusable class names helper for
[41:40] merging tail class names. Although I
[41:43] think it would do this by default, it's
[41:45] good to mention it. Finally, we want to
[41:48] ensure that all of the components match
[41:50] the existing dark theme within
[41:52] globals.css.
[41:54] And then we want to apply some checks
[41:56] when it is done. For example, we want to
[41:59] make sure that all components import
[42:01] without errors, that the CN works
[42:03] properly, and that no default light
[42:06] styling appears. This is what we call a
[42:09] feature specification or a feature spec.
[42:12] Every unit we build from here on has
[42:14] one. The spec tells the agent exactly
[42:18] what to do, exactly what not to touch,
[42:21] and how to verify when it's done. No
[42:23] guessing. So let's open up our agent by
[42:26] pressing commandshift I. As I said, you
[42:28] can use anyone. I'll use claw code. I'll
[42:32] start a new chat. And you can even open
[42:34] up that file which will automatically
[42:36] put it within its context. And then you
[42:38] can tell it something like read add01
[42:42] design system update the progress
[42:46] tracker MD file to mark this as in
[42:50] progress and then implement exactly as
[42:55] specified. This is the same template
[42:57] we'll use often, but the only thing
[42:58] that's going to change is going to be
[43:00] the spec of the feature we're
[43:02] developing. So let's go ahead and run
[43:04] it. And notice what will happen before
[43:06] the agent writes a single line of code.
[43:09] It'll read the specification and then
[43:11] update the progress tracker. You can see
[43:14] how it's going through all the files we
[43:16] prepared for it. And only once it has
[43:18] enough context, it'll write and save the
[43:20] plan and then execute it. And only when
[43:23] it has a full plan, it will update the
[43:25] progress tracker.md and then start doing
[43:28] it. So we can already take a look at the
[43:30] progress tracker. And I'll open it up so
[43:33] we can see what it is doing. And you can
[43:35] see that the current phase is feature01
[43:38] system design. The current goal to
[43:40] install and configure shaten with dark
[43:42] theme. And that is currently in progress
[43:45] with the feature 02 to be done. And it's
[43:48] also adding the architectural decisions
[43:50] needed for every step as well as the
[43:52] session notes. It's going to ask us
[43:54] whether want to run this command to
[43:56] install shaden. So I'll say yes, go
[43:58] ahead. And after it installs everything,
[44:00] it'll verify it with TypeScript. It
[44:03] looks like it completed with zero
[44:04] errors. And finally, it needs to update
[44:06] the progress tracker to completed. So we
[44:10] can already open it up right here under
[44:12] progress tracker. And it should move it
[44:14] from current phase over to completed. So
[44:18] now at any point in our application if
[44:20] we come back two months later it'll know
[44:23] that it's using SHAT CN tailwind v4 with
[44:26] the following components only using dark
[44:28] theme and all the additional helpers as
[44:31] well as the architectural decisions. So
[44:33] once it finishes the agent will have
[44:36] configured chat installed the components
[44:38] and verified it all works. So, what do
[44:41] you say that we test it out? Back on
[44:43] localhost 3000, the first good sign
[44:45] should be that we are now officially in
[44:47] dark mode. And if you head over to the
[44:50] homepage, that's going to be within app
[44:52] page. We can try to use a chaten button
[44:55] component coming from components UI
[44:58] button. And we can try to make it say
[44:59] something like click me. You can see
[45:02] it's coming from there. And it follows
[45:04] our UI theme. That's it. Our first
[45:07] feature being the theming and chassis
[45:09] and setup is done. And that's the
[45:11] spectrum workflow I was telling you
[45:13] about. We define the specifications. We
[45:16] run the prompt. We verify the output.
[45:19] And then we move on. But just before we
[45:21] move on to our second feature, I want to
[45:24] add just one little extra step to this
[45:27] whole workflow that's going to make our
[45:28] codebase even more scalable,
[45:30] predictable, and less errorprone. and
[45:33] that is whenever we implement a specific
[45:35] feature, let's also review it with code
[45:38] rabbit. There's been a report that says
[45:40] that AI code creates 1.7 times more
[45:43] problems, which means that even though
[45:44] we're faster, we're producing more
[45:47] issues per PR. Also, the code becomes
[45:50] less readable naturally and the error
[45:52] handling isn't being done properly.
[45:54] Security also suffers. So, let's add
[45:57] that one additional line of defense.
[45:59] Let's review every single feature that
[46:01] we add to our project. In the same way
[46:03] that biggest teams such as the
[46:05] developers over at Nvidia are doing it.
[46:07] I'll leave the link down in the
[46:08] description so you can create your free
[46:10] account and follow along. You can log in
[46:12] with GitHub. And once you're in, you'll
[46:15] be able to see that I already gave it
[46:16] access to many of my repos. But first,
[46:18] we got to push our project over to
[46:20] GitHub. So, head over to github.com/new
[46:24] and create a new repo. You can call it
[46:27] ghostai.
[46:30] and just create it. Next, you can copy
[46:32] these commands one by one or you can
[46:35] just copy all of them together. Open up
[46:37] your agent and paste it. Then press
[46:40] enter. It's going to ask us whether
[46:42] we're going to allow it to stage all the
[46:43] changes. So, I'll say yeah, go ahead.
[46:46] And they'll also allow all future
[46:47] commits as that's going to help us speed
[46:49] up the workflow as well as adding a
[46:51] remote. And finally, push. You can see
[46:54] that the changes have been pushed
[46:55] successfully. So if you come back and
[46:57] reload, you'll be able to see the
[47:00] current list of changes over on the
[47:02] repo. It's always good to make your
[47:04] project descriptive. So you can remove
[47:06] the releases, deployments, and packages
[47:08] and add a short description such as
[47:11] Ghost AI is an interactive systems
[47:16] architecture
[47:19] builder. We can route to the deployed
[47:21] website. For now, I'll just route it to
[47:23] jsmastery.com. And here we can put the
[47:25] different topics such as Nex.js,
[47:28] React, Live Blocks, Clerk, Trigger Dev,
[47:33] and even Code Rabbit, which we'll be
[47:35] using for reviewing your code. And I
[47:37] like how AI always adds nice commit
[47:39] messages and not random gibberish that
[47:41] I'm used to. But yeah, now back within
[47:44] Code Rabbit, you can head over to add
[47:46] repositories,
[47:47] sign in, and give it access to all your
[47:50] repos. And then when you're back, you
[47:52] can just find your project right here,
[47:58] which means that it's automatically
[47:59] being tracked. So as soon as we start
[48:01] adding real features to the app, we'll
[48:03] be able to open up a PR for every new
[48:05] feature as we're developing within a
[48:07] large organization and then get it
[48:09] reviewed and only when Code Rabbit gives
[48:11] it a green light, merge it over to main.
[48:16] Now that our colors are in and the
[48:18] initial chassis components are in as
[48:20] well, we are ready to start building the
[48:22] actual application and the first thing
[48:24] that we need is the editor including the
[48:27] top navbar and the left sidebar because
[48:29] they're the foundation of every feature
[48:31] we're going to build from here on. We're
[48:33] not yet touching off and we're not
[48:35] building this project creation. We just
[48:37] need to establish the layout so when
[48:39] these features come, they have somewhere
[48:41] to go. So inside of feature specs
[48:44] folder, create a new file called 02
[48:47] editor.md.
[48:49] And within it, we're going to follow a
[48:51] similar structure we followed before. We
[48:53] want to start with explaining what we
[48:55] need, such as the base Chrome components
[48:58] that frame every editor screen, the top
[49:00] knob bar and the left sidebar shell.
[49:04] These will be reused and extended in
[49:06] every chapter that follows. Then we need
[49:08] to focus on what are we actually
[49:10] creating. That's going to be the editor
[49:13] navbar. So we wanted to create a new
[49:15] component within the editor editor
[49:17] navbar file. And then we want to specify
[49:20] some requirements that follow. We want
[49:23] this navbar to be of a fixed height at
[49:25] the top. We want it to have both left,
[49:28] center, and right sections, which you
[49:30] can see right here. On the left, we open
[49:32] up the sidebar. In the middle, we have
[49:34] the name. And on the right side, we have
[49:36] additional actions. That's exactly what
[49:38] we explained right here.
[49:41] And of course, it's going to be of a
[49:42] dark background with a subtle bottom
[49:45] border. Next, we want to explain what we
[49:47] want to do with the project sidebar. So,
[49:49] right below, we can say create a project
[49:52] sidebar component. It should float above
[49:55] the editor canvas. Opening it should not
[49:58] push the page content. So, you can see
[50:01] it remains where it is and slides in
[50:04] from the left. It has the header that
[50:06] says projects and title and a close
[50:09] button right here. It can use the shhats
[50:11] and tabs component and both tabs show
[50:14] empty placeholder state full width new
[50:16] project button at the bottom with the
[50:19] plus icon. So something like this. Oh
[50:21] and finally when we click create new
[50:23] project we need this kind of a dialogue
[50:26] uh a new popup that shows.
[50:29] So for that we can say something along
[50:31] the lines of
[50:33] dialogue pattern use the existing color
[50:36] tokens from globals for dialogue
[50:38] styling. It supports title description
[50:40] and footer action but don't build any
[50:42] dialogues yet. We just want to create
[50:45] the component for it. Finally to check
[50:47] whether it is done we can check whether
[50:50] new components compile without
[50:51] TypeScript errors, no lint errors and
[50:54] diagram pattern is ready for future use.
[50:57] So hopefully you were typing this out
[50:59] with me or maybe you paused the screen
[51:01] and typed it with your own words. But
[51:03] this course isn't at all about typing.
[51:06] It is about understanding what we're
[51:08] doing right here. So if you don't really
[51:10] feel like typing, nor you should. In the
[51:12] video kit link down in the description,
[51:14] I'll provide you with all the prompts
[51:16] that we're going to use throughout the
[51:18] rest of this course. So, if at any point
[51:20] I'm going too fast when explaining them
[51:23] and you just want to have it on your end
[51:25] and listen along, you can totally do
[51:28] that. But yeah, let me quickly walk you
[51:30] through the structure because this is
[51:31] the template that every spec file in
[51:33] this project will follow. We start with
[51:35] a goal, one or two sentences. What does
[51:38] this unit produce when it is done? Then
[51:41] we go over some specific design
[51:43] decisions. Is it visual or structural or
[51:46] something specific to the component like
[51:48] layout behavior responsiveness? And this
[51:51] is where we can refer to that UI context
[51:53] file so that the agent isn't guessing
[51:55] the colors. Then we go over into
[51:58] implementation. And in this case, I
[52:00] decided to separate it into sections. So
[52:03] we have the editor navbar, the project
[52:05] sidebar, and the dialogue pattern. And
[52:08] finally, the verification checklist. So
[52:10] let's open up our agent. Whenever you're
[52:12] building a new feature, always open up a
[52:15] new chat and don't use one of the older
[52:17] chats. That's because we don't want some
[52:19] stale context lingering around. Only
[52:21] remain within the same chat when what
[52:23] you're about to do next is related to
[52:25] what you've done before, such as when
[52:27] you want to fix specific issues. You can
[52:29] see that it already has access to the
[52:31] editor file. So I'll say read this file
[52:35] and update the tasks on the progress
[52:41] tracker and then implement it
[52:45] exactly as specified
[52:48] and press enter. And in about a minute
[52:51] it's all done. It developed the editor
[52:53] navbar the sidebar and also the dialogue
[52:57] pattern. Type script and eslint both
[53:00] pass clean. Progress tracker also got
[53:02] updated. So let's check the progress
[53:04] tracker first. It'll be right here
[53:06] within the progress tracker. So if you
[53:09] check feature 2 completed, editor navbar
[53:13] and project sidebar both implemented.
[53:16] You can see them right here under editor
[53:18] editor navbar and project sidebar. We
[53:21] just created them so far, but they're
[53:23] not yet being used within the layout.
[53:25] And even though this wasn't part of the
[53:27] checks, I want to actually be able to
[53:30] see them. I want to tell it to use the
[53:32] navbar and the sidebar right now within
[53:34] the project. So I'll open up the chat in
[53:37] the same context window and tell it to
[53:40] use these two components within a
[53:42] layout. And within a minute, it put it
[53:44] to use. It even created a placeholder
[53:46] page. So we can navigate over to the
[53:47] editor and check it out. So head over to
[53:51] localhost 3000/editor
[53:53] and you can see a canvas coming soon but
[53:56] there is a top bar and a left sidebar
[53:59] which opens up the projects. So you can
[54:01] see that what we requested indeed got
[54:03] implemented. Since we're not yet at the
[54:06] point where we need that because we
[54:07] don't even yet have the editor. I
[54:09] actually want to show you how you can
[54:11] undo the changes at least right here in
[54:13] cloud code. The only thing you have to
[54:14] do is press this back arrow on the
[54:17] message that you used to create these
[54:18] components and then say rewind code to
[54:21] here which is going to bring us back and
[54:23] only give us what the specification
[54:25] wanted and that is the components that
[54:28] we can then use and that compile but
[54:30] we're not using them quite yet. Perfect.
[54:32] So now that we have the navbar and a
[54:34] toggable sidebar, let's quickly check
[54:37] them out. The editor navbar is pretty
[54:39] straightforward. And the sidebar accepts
[54:41] some props such as is open and on close
[54:44] and uses the chats and tabs to modify
[54:46] what's being shown. But when you're
[54:48] writing code yourself, you have a
[54:50] natural understanding of every decision
[54:52] you made. Heck, you wrote it. You know
[54:55] why a function is structured in a
[54:57] specific way or why you used specific
[54:59] props.
[55:01] But AI generated code doesn't come with
[55:04] that context. The agent made decisions
[55:08] that were reasonable most of the time,
[55:10] but you didn't make them. And that means
[55:13] that reviewing AI output isn't optional.
[55:15] It's the step that keeps you in control
[55:17] of your own codebase. So, that's the
[55:19] perfect use case to test out the code
[55:21] rabbit edition that we added in the last
[55:23] lesson. I'll open up the chat and tell
[55:25] it to push all the current changes to a
[55:29] new branch called development. Typically
[55:32] in real production databases, you often
[55:34] have multiple branches such as dev,
[55:37] staging, and only then main. So for now,
[55:40] we want to push this over to the
[55:42] development branch, get it reviewed, and
[55:44] only if it's good, merge it over to
[55:46] main. So by giving it this quick
[55:48] message, it'll run a couple of git
[55:50] commands, figure out that we're
[55:52] currently on main, that we need to
[55:54] switch over and push to that new branch.
[55:56] And that's a little pro tip. Uh, I mean,
[55:59] sure, you could run these commands
[56:01] through the terminal, but I find it
[56:03] super easy to just stay in flow and tell
[56:05] the agent to push the code for me, which
[56:08] you can see it just did. So, if you head
[56:10] back over to your repo, you'll see that
[56:12] the development branch had recent pushes
[56:14] 3 seconds ago. So, let's go ahead and
[56:16] compare them and open up the pull
[56:18] request. We have 333 new lines of code
[56:22] across five different files. So, Code
[56:24] Rabbit immediately hooked itself onto
[56:26] the PR and we'll see whether it'll be
[56:28] able to pull out some bugs out of the
[56:30] hat. Let's give it a minute and then
[56:33] I'll be right back. And we got back the
[56:35] walkthrough where it says exactly what
[56:38] we introduced in this project such as
[56:40] two new React components for an editor
[56:42] UI Chrome, an editor navbar, and a
[56:45] project sidebar. These are super simple
[56:47] as this was a simple review. Later on,
[56:50] these are going to get much more
[56:52] detailed. But yeah, let's check whether
[56:54] we have some potential issues even on a
[56:56] simple PR such as this one. There's one
[56:58] major issue that says hide the offscreen
[57:01] sidebar from focus order and assistive
[57:04] tech when closed. So specifically, this
[57:06] is an accessibility fix, which is
[57:08] definitely a good implementation. Since
[57:10] we haven't yet utilized this component
[57:12] in our app, I'll leave this so we can
[57:14] add it later. There's also a minor issue
[57:16] where the spec lists only the is open
[57:19] for the sidebar, but the implementation
[57:22] also requires on close. So actually it's
[57:24] suggesting to change the specification.
[57:27] This is interesting because sometimes
[57:28] you're going to miss some stuff from the
[57:30] spec. And it's okay if AI tries to fix
[57:33] it or add some stuff, but it's equally
[57:36] as important for Code Rabbit to flag it
[57:39] because the whole reason why we're
[57:40] writing specs in the first place is so
[57:42] we can have predictive output. So
[57:44] basically you can just copy this part
[57:46] right here. Go back to your codebase
[57:48] where we're saying accepts and then it's
[57:51] going to be is open prop but we're going
[57:53] to say accepts both is open and on close
[57:57] props. Little change I know but now our
[58:00] codebase is consistent with the spec.
[58:03] And that's it for this simple PR. As we
[58:05] continue developing more components the
[58:07] reviews are going to get significantly
[58:09] more detailed. So for now, I'm going to
[58:11] go ahead and merge it, which means that
[58:13] we are ready to continue developing the
[58:15] next component.
[58:18] For this type of application, we don't
[58:21] really need a traditional homepage. Most
[58:24] tools like this drop you straight into
[58:26] the editor. You sign in from a simple
[58:29] sign-in page and you manage everything
[58:32] from the canvas. And that's exactly what
[58:34] we'll do within our app. But we need O
[58:38] sign in, sign up, and other similar
[58:40] pages where you explain how your
[58:42] application works and then allow users
[58:44] to sign back in. So to get that set up,
[58:47] click the clerk link down in the
[58:49] description and sign in. You can sign in
[58:51] with Google or GitHub. And once you're
[58:53] in, you can head over to applications
[58:55] and create a new app on the dashboard.
[58:58] You can give it a name such as ghost AI
[59:01] and choose the sign-in options such as
[59:04] email, Google and since this is a
[59:06] development website, we can also do
[59:08] GitHub. Then click create application.
[59:11] We are building on Nex.js. So what you
[59:14] can do is just install add clerk/nextgs
[59:17] by copying this command and paste it
[59:20] straight into the terminal. And while
[59:23] that is being installed, you can also
[59:24] set up your clerk API keys by copying
[59:27] them from here and creating a new file
[59:30] called env.local
[59:34] and then paste them right here. Now,
[59:36] before we hand anything over to the
[59:38] agent, there are two things you need to
[59:40] know about clerk and nex.js16
[59:42] specifically because if you skip this,
[59:45] the agent will get it wrong. And it says
[59:47] it right here. If you're using Nex.js
[59:49] JS15 or lower, name your file
[59:52] middleware.ts instead of proxy.ts.
[59:56] The code itself remains the same. Only
[59:58] the file name changes. But because most
[1:00:00] agents were trained on NexJS 14 and 15
[1:00:03] code bases, it'll almost certainly
[1:00:06] create a middleware.ts file by default.
[1:00:09] So we'll have to specify proxy.ts
[1:00:11] explicitly in our spec so it doesn't
[1:00:13] have to guess. Oh, and another important
[1:00:16] thing is that just by adding middleware,
[1:00:18] it doesn't automatically protect all
[1:00:20] routes. As you can see right here, by
[1:00:23] default, it leaves all the routes
[1:00:25] public. And this catches a lot of
[1:00:27] developers. You have to explicitly
[1:00:28] define which routes are protected and
[1:00:31] which are public, which means that we
[1:00:33] have to configure everything
[1:00:34] intentionally. And this is exactly why
[1:00:36] reading the updated documentation before
[1:00:38] building with AI matters. The agent
[1:00:41] knows Clerk, not necessarily the version
[1:00:43] of Clerk you just installed or the
[1:00:45] version of Nex.js you're running on. The
[1:00:47] spec bridges that gap. Oh, but we can
[1:00:49] also use agent skills. As I told you at
[1:00:52] the start, most major frameworks and
[1:00:55] libraries now publish official skill
[1:00:57] packages specifically for this problem.
[1:00:59] It gives your agent up-to-date
[1:01:01] knowledge, current APIs and patterns,
[1:01:04] and the best practices of the library
[1:01:05] you're using. So, if you search on
[1:01:07] Google or within the docs clerk agent
[1:01:10] skills, you'll be redirected to this
[1:01:12] page. Then, simply copy the installation
[1:01:14] command. Head back over to your codebase
[1:01:17] and paste it in your terminal. MPX
[1:01:20] skills add clerk skills. Press enter.
[1:01:24] You might need to install the skills
[1:01:25] package by saying Y and then enter. And
[1:01:28] then by pressing the arrow up and down
[1:01:31] keys and the space key, you can select
[1:01:33] specific packages such as core clerk,
[1:01:36] you can either select some additional
[1:01:38] clerk features or some additional clerk
[1:01:40] frameworks like in this case I'm going
[1:01:42] to go with clerk next.js patterns and
[1:01:46] press enter. Then you can select
[1:01:49] additional agents that you want to add
[1:01:51] it to. By default, it's going to work on
[1:01:53] codeex cursor anti-gravity. But if you
[1:01:56] want to add clot code, you have to
[1:01:58] select it here and press enter. And we
[1:02:00] can install it in project scope via sim
[1:02:03] link. That's the recommended way. So
[1:02:06] just proceed with installation. Perfect.
[1:02:08] Our skill is installed and we'll be able
[1:02:10] to invoke it later on once we focus on
[1:02:12] implementing the odd functionality.
[1:02:15] So now we are ready to write the spec.
[1:02:19] Open up your context feature specs and
[1:02:21] create a new file called 03 o.md.
[1:02:26] And once again, the full feature specs
[1:02:28] files are linked in the description in
[1:02:30] case you want to just copy them and then
[1:02:32] follow along or you can slowly type it
[1:02:34] out with me. Let's start by telling it
[1:02:37] that clerk is already installed and
[1:02:39] connected. So we just need to wire it
[1:02:41] into the next.js GS app provider o pages
[1:02:45] redirects route protections and the user
[1:02:48] menu. When it comes to the design, we
[1:02:52] just want to use the clerk's dark theme
[1:02:54] from the add clerk UI themes as the
[1:02:57] base. And then we want to override the
[1:02:59] clerk appearance variables using the
[1:03:01] app's existing CSS variables
[1:03:05] with no hard-coded colors for the sign
[1:03:08] up and signin pages. This is what we
[1:03:11] want to develop on large screens. We
[1:03:14] just want to have a simple two panel
[1:03:16] layout. On the left side, a logo, a
[1:03:19] tagline, and texton features. On the
[1:03:22] right side, a centered clerk form. And
[1:03:25] on small screens, forms only. We don't
[1:03:28] want to have any kind of gradients as
[1:03:30] that's going to seem AI-ish. No
[1:03:32] oversized hero sections, cards, or
[1:03:34] scrollheavy layouts. Keep the layout
[1:03:36] minimal and professional. And then we
[1:03:39] can dive into a bit more details on the
[1:03:41] full implementation.
[1:03:44] So we can say wrap the root layout with
[1:03:48] the clerk provider using the clerk's
[1:03:50] dark theme. Create sign in and sign up
[1:03:53] pages using clerk components. And as I
[1:03:56] told you before, we have to be specific
[1:03:58] and telling it that it should use the
[1:04:00] proxy.ts file name at the project route
[1:04:03] instead of the middleware.ts.
[1:04:06] And then we have to define public routes
[1:04:08] using the existing sign in and sign up
[1:04:10] environment variables protect everything
[1:04:13] else by default which means that we have
[1:04:16] to update our homepage so that when
[1:04:19] authenticated users visit it we redirect
[1:04:22] them to the editor or when
[1:04:24] unauthenticated users visit it we
[1:04:26] redirect them to the sign-in page. We
[1:04:30] also want to implement Clerk's built-in
[1:04:33] user button to the editor navbar right
[1:04:36] section for profile settings and logout.
[1:04:38] We want to keep clerk's default user
[1:04:40] menu and profile flows intact and not
[1:04:43] rebuild heavily customized clerk
[1:04:45] internals and want to use existing clerk
[1:04:48] environment variables without renaming
[1:04:50] or inventing new ones. Finally, we can
[1:04:53] specify additional dependencies such as
[1:04:56] clerk UI if we need to install it. And
[1:04:58] then when it's done, we want to check
[1:05:00] that proxy file is there, that all
[1:05:03] routes are protected except public off
[1:05:06] routes. All pages use CSS variables with
[1:05:09] no hard-coded colors. Clerk provider
[1:05:12] wraps the layout and the build passes.
[1:05:15] This is our complete authentication
[1:05:17] implementation. Now you know the drill.
[1:05:20] Go ahead and open up your agent. Give it
[1:05:23] access to this file and tell it to read
[1:05:26] this file and update the progress
[1:05:28] tracker.md file accordingly. Then
[1:05:32] implement the o feature exactly as
[1:05:34] specified in the o.md file. Okay, you
[1:05:38] can see that the built-in microphone
[1:05:40] feature right here still isn't perfect.
[1:05:42] Let me try to do the same thing with
[1:05:43] whisper flow specified in o.md file.
[1:05:50] There we go. That's a bit better. And
[1:05:52] specifically, it's 03.
[1:05:54] MD. Perfect. Let's go ahead and run it.
[1:05:58] First, it's asking me to run some bash
[1:06:00] commands to check whether clerk has been
[1:06:02] properly installed. And we'll say, yeah,
[1:06:05] go ahead. You can run it. It took him
[1:06:07] about 2 minutes or so to go through all
[1:06:10] the context we shared. And only then
[1:06:12] it'll start to implement everything in
[1:06:14] parallel. And this is much better than
[1:06:17] if it started right away and then just
[1:06:19] ended up with a bunch of mistakes. So
[1:06:21] the list of updates that it put right
[1:06:23] here is to update the env.local with
[1:06:26] clerk signin and signup URL varss.
[1:06:29] Create a proxy with clerk middleware
[1:06:31] route protection. Update the app layout
[1:06:33] with the clerk provider and dark theme.
[1:06:36] Create signin and signup pages with a
[1:06:38] two panel layout. Update the app page to
[1:06:41] redirect based on the off state. add the
[1:06:44] user button to editor navbar and create
[1:06:46] editor page and then update the progress
[1:06:49] tracker and run mpm run build to verify.
[1:06:52] It's going to ask me whether it has the
[1:06:54] ability to create some directories and
[1:06:56] I'll tell it, yeah, go ahead. And in the
[1:06:59] future, we can give it some more
[1:07:00] permissions so it can do things a bit
[1:07:02] more freely. And after it came up with
[1:07:04] the initial plan, it actually built out
[1:07:07] everything pretty quickly, maybe even in
[1:07:10] less time than it used to think how to
[1:07:12] approach it in the first place, which
[1:07:14] shows you just how important the initial
[1:07:17] context and a proper task are. And there
[1:07:19] we go. The build passes. And here's the
[1:07:22] summary of everything that was
[1:07:23] implemented. I think all of these things
[1:07:26] right here shouldn't come as a surprise
[1:07:28] because we initially specified them in
[1:07:31] this spec. Then it updated the to-dos
[1:07:34] and now it just did it. And yeah, it's
[1:07:36] pretty interesting that it even notes
[1:07:38] right here that it would have gotten
[1:07:40] confused about this middleware proxy
[1:07:42] thing if we didn't specify it properly.
[1:07:44] But thankfully, it did it in the right
[1:07:46] way thanks to the research that we've
[1:07:48] done at the start. So, what do you say
[1:07:50] that we take it for a spin? The
[1:07:52] application is running on localhost
[1:07:54] 3000, but whenever I make some bigger
[1:07:56] changes, I like to rerun it. But
[1:07:58] initially, if you head over to
[1:08:00] localhost, you might get redirected to
[1:08:02] this clerk handshake part, which is
[1:08:04] going to lead to a broken page. But
[1:08:07] after you reload, it should properly
[1:08:09] redirect you back to the homepage. And
[1:08:11] after that, it should just work. This is
[1:08:14] something that we can polish and fix up
[1:08:16] later on. But yeah, this is looking
[1:08:19] interesting. Definitely not quite as
[1:08:22] nice as the original application that
[1:08:24] I've showed you that's deployed. So,
[1:08:27] what are some of the things that we can
[1:08:28] do to make it look more similar to that
[1:08:31] one? Well, step one is to search some
[1:08:34] kind of design websites online like
[1:08:36] Dribble or award-winning websites and
[1:08:39] then just take a screenshot and try to
[1:08:41] get it to match to that closer. Or in
[1:08:44] this case, you can head over to the
[1:08:45] deployed version of this application,
[1:08:48] take a screenshot of this whole UI that
[1:08:51] you can see right here, and then we can
[1:08:53] feed it over into our chat. So, go ahead
[1:08:56] and open up the chat. Keep in mind that
[1:08:58] we can still stay within the
[1:08:59] authentication window that we worked on
[1:09:02] because now we're fixing some parts
[1:09:04] about that specific implementation. So,
[1:09:06] what you can do is just click this plus
[1:09:08] right here and upload from computer or
[1:09:11] just drag and drop the screenshot. then
[1:09:13] select it. And then we can further point
[1:09:15] out to some things that could be
[1:09:17] improved, not just the layout. It seems
[1:09:20] like it didn't properly read the fonts
[1:09:22] that the right side of the screen is
[1:09:24] taking a larger portion. So maybe we can
[1:09:26] split them 50/50, same as it is right
[1:09:29] here, and make the font size a bit
[1:09:31] larger. So it's not just the layout. We
[1:09:33] needed to review the screenshot and
[1:09:35] update the UI of our current application
[1:09:38] to look more like the one on the
[1:09:40] screenshot. means 50/50 left and right
[1:09:43] side layout with some kind of a color on
[1:09:46] the left side to differentiate it from a
[1:09:48] dark background as well as we need to
[1:09:50] fix the fonts so that it uses the ones
[1:09:53] outlined in our UI guidelines. I think
[1:09:56] for now this is going to be enough for
[1:09:58] it to get closer to the design we want
[1:10:00] to get. So press enter and let's see how
[1:10:02] it handles it. And there we go. The
[1:10:04] build passes. It updated the globals
[1:10:07] from circular font reference to the one
[1:10:10] that should be correct right now. The
[1:10:12] body was pointing at itself. So, this
[1:10:14] font was never actually applied to
[1:10:16] anything. Same fix for the heading. And
[1:10:18] it also implemented some other fixes.
[1:10:20] Let's check it out. The design now looks
[1:10:22] much closer to the finished product. The
[1:10:25] fonts are being properly applied and
[1:10:27] that makes a big difference. So does the
[1:10:30] increase in font size and this shift
[1:10:32] between the two different background
[1:10:34] colors. Of course, later on we can come
[1:10:36] up with a unique logo that we can put
[1:10:38] right here. But for now, this is looking
[1:10:41] great. And believe it or not, we have a
[1:10:44] fully functional authentication system
[1:10:46] built in right here. So, what do you say
[1:10:48] that we go ahead and test it out? You
[1:10:50] can head over to signup to see whether
[1:10:52] that works. And it does. Later on, if
[1:10:55] you want to, you can modify the contents
[1:10:56] on the left side depending on whether
[1:10:58] you're in sign in or sign up page. And
[1:11:01] then let's use something like GitHub to
[1:11:03] sign in. I'll authorize it. And the
[1:11:06] redirect redirects us to a page that
[1:11:09] currently breaks. So I'll try to head
[1:11:11] back over to localhost 3000 one more
[1:11:13] time. And now when we get back, it
[1:11:16] actually redirects to the editor
[1:11:18] properly. You can see that we have the
[1:11:21] sidebar. We have a space for the canvas
[1:11:24] that's about to come in the future. And
[1:11:26] then on top right, we see all the
[1:11:28] information about our currently logged
[1:11:30] in account, which is beautiful. I mean,
[1:11:32] we get complete user management within a
[1:11:34] single prompt that we've done. Let's
[1:11:36] also try to sign out for now. And we do
[1:11:39] get one issue when we click that button
[1:11:41] saying there's an unexpected response
[1:11:43] received from the server. So, if we head
[1:11:45] back over here and open up the terminal,
[1:11:48] we can see an unhandled rejection.
[1:11:50] Unexpected response was received from
[1:11:52] the server. And then in the terminal, we
[1:11:54] see something like this, which doesn't
[1:11:56] really tell us much. Now, what we could
[1:11:58] do is just copy this, open up the chat
[1:12:02] window one more time by heading over
[1:12:04] here, and then just pasting this error
[1:12:06] and telling it to fix it. But I'm
[1:12:08] actually glad that this error happened
[1:12:10] because I can teach you a bit better and
[1:12:12] more precise way to handle these issues
[1:12:15] and so that when you try to fix them,
[1:12:17] you don't cause new ones. So instead of
[1:12:20] pasting this right into the chat, we're
[1:12:22] actually going to open up a new file
[1:12:24] right here within context and call it
[1:12:27] current issues.md.
[1:12:31] You can even do it within feature specs.
[1:12:33] Either way works. Then you can paste any
[1:12:36] kind of errors that you have and explain
[1:12:38] what's happening. So I'll explain that
[1:12:41] when I click the log out button
[1:12:46] the following error appears and now I
[1:12:49] can paste this error message and we can
[1:12:51] also specify that sometimes when we log
[1:12:54] in we get redirected to this weird long
[1:12:57] URL which doesn't show anything on the
[1:12:59] page and then we can just paste this URL
[1:13:03] right here. Again, the errors on your
[1:13:06] end might be a bit different from what
[1:13:08] I'm seeing right here. Whatever they
[1:13:10] are, I don't want to teach you how to
[1:13:12] copy and paste. I want to teach you how
[1:13:14] to solve the problems for yourself.
[1:13:16] Explore the current issues file and
[1:13:19] deeply analyze the problem. Only when
[1:13:22] you have the analysis, give it back to
[1:13:24] me with the idea of how you're planning
[1:13:27] to solve it and then wait for me to give
[1:13:29] it the green light to execute it. So
[1:13:32] yeah, writing something like this makes
[1:13:33] sense because that way it doesn't go
[1:13:35] into the spiral of trying to fix its own
[1:13:37] bugs while breaking 10 other things. You
[1:13:39] provided the error. It's going to come
[1:13:41] back with the analysis. You're the one
[1:13:43] deciding whether that analysis makes
[1:13:45] sense and whether it can actually
[1:13:47] execute it. So let's run it and see what
[1:13:50] it comes back with. And after some
[1:13:53] thinking, it's back with the analysis.
[1:13:55] And this is so much better and so much
[1:13:58] more detailed than if we just told it to
[1:14:00] fix it immediately. Now it actually
[1:14:03] tried it out and has a deep idea of
[1:14:05] what's happening. The server log is the
[1:14:07] key clue. Proxy took 373 milliseconds
[1:14:11] out of a half a second total request.
[1:14:13] Almost all time is spent in the proxy.
[1:14:16] So that already points it in the right
[1:14:18] direction. As a human person, I would
[1:14:21] never figure this out on my own. at
[1:14:23] least not from such a vague error
[1:14:25] message. But yeah, here it figures out
[1:14:28] that this button needs an after sign out
[1:14:30] URL. So it's just going to add it. And a
[1:14:33] similar thing is happening with the
[1:14:35] handshake URL. It basically needs to
[1:14:38] configure that after signup URL and that
[1:14:41] way it's going to route it properly. So
[1:14:43] it provided a twoix plan. So this looks
[1:14:46] plausible to me. Looks good. So let's
[1:14:48] just tell it to execute the plan and fix
[1:14:51] the issues. There we go. So, the fix now
[1:14:54] seems very apparent. We just needed this
[1:14:57] after sign out URL. And if you want to
[1:14:59] learn more tips and tricks just like
[1:15:01] this one about actually analyzing and
[1:15:03] fixing the errors and how I approach
[1:15:06] building these production level
[1:15:07] applications, definitely check out the
[1:15:09] specdriven agentic development course.
[1:15:11] It's not out yet as it's going to be
[1:15:13] super detailed and it's going to follow
[1:15:15] the best practices from the strongest
[1:15:17] developer teams out there. But yeah,
[1:15:19] it'll be out soon. But I'm still super
[1:15:21] glad that while I'm developing that, you
[1:15:23] can still learn how I develop these
[1:15:26] applications with the agentic ways with
[1:15:28] this new video that you're watching
[1:15:30] right now. And you can let me know down
[1:15:32] in the comments how you like this new
[1:15:34] type of video. I get that it's
[1:15:36] completely different from manual coding,
[1:15:38] but I still think there's so much to
[1:15:40] learn and we can have a predictable
[1:15:43] development workflow even with AI doing
[1:15:46] the writing for us. So let's see whether
[1:15:49] this actually fixes it. And the build
[1:15:51] passes. The after sign out URL prop was
[1:15:54] removed from the user button as it
[1:15:55] belongs in clerk options and is set via
[1:15:58] environment variables. So we'll soon be
[1:16:00] able to verify whether that actually
[1:16:02] fixes it. But before I want to open up
[1:16:05] my terminal, stop it from running and
[1:16:07] then rerun it again on localhost 3000
[1:16:10] because we changed the env. So we want
[1:16:12] to make sure that they're read by the
[1:16:13] browser. So now heading back over to
[1:16:16] localhost 3000. Maybe you're signed in
[1:16:18] already, which is fine. You can simply
[1:16:20] sign out now. And that brings us to
[1:16:22] another error, which is the same one
[1:16:24] we've had before. And another thing you
[1:16:26] can do is head over to inspect element,
[1:16:28] switch over to the application tab, and
[1:16:31] then clear all the cookies. So find the
[1:16:33] cookies for localhost 3000, clear them,
[1:16:36] and then reload the page. You'll be
[1:16:39] redirected back to the homepage. And now
[1:16:41] we can retry with a clean slate. So,
[1:16:44] I'll sign in using GitHub the same way I
[1:16:46] did before. That works. I automatically
[1:16:48] got redirected over to the editor, which
[1:16:51] is great. And now I'll sign out. And
[1:16:53] that worked. So now head back over
[1:16:56] within your terminal. Run git add dot
[1:16:59] git commit-m implement o and then get
[1:17:03] push. This is going to push all the
[1:17:05] changes to origin development allowing
[1:17:08] us to open up a pull request over to the
[1:17:10] main branch. Then you can open up a PR
[1:17:14] and let's wait for Code Rabbit to review
[1:17:16] it. This time we had many changes but
[1:17:19] not many of them are directly related to
[1:17:21] what we did in the code. We just added
[1:17:23] these agent skills so that everybody
[1:17:26] else's agents working on this codebase
[1:17:28] also well become smart in the
[1:17:30] technologies that we're using for the
[1:17:32] project. And then yeah of course we
[1:17:34] implemented a couple of different files
[1:17:36] that Code Rabbit will verify. But
[1:17:38] primarily what we've done is right here
[1:17:41] within app signin and signup pages we
[1:17:45] have added some features that would
[1:17:46] display on the left side and then the
[1:17:49] sign-in page where on the right side we
[1:17:52] just render the signin component coming
[1:17:54] from clerk. Similar thing happens over
[1:17:58] to the signup page. So right here we're
[1:18:01] just rendering the signup UI. Then over
[1:18:05] in the layout, we are wrapping
[1:18:07] everything with a clerk provider,
[1:18:09] setting the theme to dark, and setting
[1:18:12] some custom variables. That's it.
[1:18:14] Everything else remains the same. And
[1:18:16] then within the editor page, we're
[1:18:18] simply showing the navbar and the
[1:18:20] sidebar as well as the rest of the
[1:18:22] content. In the navbar, we display the
[1:18:25] clerk user button, allowing us to see
[1:18:27] more info about the user and allowing us
[1:18:30] to log us out. Pretty straightforward so
[1:18:32] far. As our components and features get
[1:18:34] more detailed, we're going to do deeper
[1:18:36] dives into the codebase. But so far so
[1:18:39] good. Let's wait for the review. And
[1:18:41] quickly, we're back with a full
[1:18:43] walkthrough. This pull request
[1:18:45] integrates clerk o into a nextjs
[1:18:48] application and establishes
[1:18:49] comprehensive agent skills for clerk
[1:18:52] integration across multiple frameworks.
[1:18:54] It also adds O middleware, signin and
[1:18:57] signup pages, clerk provider setup, and
[1:19:00] introduces five new skill definitions
[1:19:02] for supporting scripts, documentation,
[1:19:04] and so on. So, obviously, a lot of the
[1:19:07] checks right here from Code Rabbit are
[1:19:09] going to be about the skills that we set
[1:19:11] up, but we can skip those for now and
[1:19:13] focus on the ones about the actual files
[1:19:16] we implemented. In this case, it looks
[1:19:18] like there's one critical issue, and
[1:19:21] that is within the context current
[1:19:23] issues.md.
[1:19:24] Well, you never want to publish current
[1:19:26] issues to GitHub anyways because you
[1:19:29] want people to see your code and not
[1:19:31] your mistakes. Um, what we're doing here
[1:19:33] is even worse. We're exposing the
[1:19:36] handshake or the JWT token from the
[1:19:39] track docs. So, this is a real security
[1:19:42] issue. So, what we need to do is delete
[1:19:44] this file. Obviously, this won't delete
[1:19:47] it from the git history, but that's fine
[1:19:49] for us because this JWT is no longer in
[1:19:52] use. So, right here over to get ignore,
[1:19:54] I'm going to add our forward
[1:19:56] slashcontext
[1:19:58] forward slash and that's going to be the
[1:20:00] current issues.mmd
[1:20:04] file. And I'll also remove everything
[1:20:07] that is within it. Not that it matters
[1:20:10] right now because we're adding it to get
[1:20:11] ignore anyway. So let's go ahead and
[1:20:13] push those changes by saying get add dot
[1:20:16] getit commit update.getit ignore
[1:20:20] and get push. Immediately the changes
[1:20:23] will be recognized which means that we
[1:20:25] can merge this over to the main branch.
[1:20:27] And while we're here we can also head
[1:20:29] over into context on the main branch and
[1:20:32] remove the current issues file right
[1:20:34] here from GitHub by simply deleting the
[1:20:37] file and committing the changes. We can
[1:20:40] also do the same thing on the
[1:20:41] development branch by heading over to
[1:20:44] context and heading over to current
[1:20:46] issues and just removing the file so
[1:20:50] that it's no longer here and it's not
[1:20:52] going to be pushed to GitHub any longer
[1:20:53] because we added it to get ignore.
[1:20:56] Perfect. With that in mind, we've
[1:20:58] successfully implemented the full UI and
[1:21:01] functionality for the authentication
[1:21:03] within our application.
[1:21:07] Now that our authentication is done and
[1:21:09] we can actually sign into our
[1:21:11] application, let's make the sidebar
[1:21:14] actually do something. As right now it
[1:21:16] is just static. Before we hook up any
[1:21:19] real data, we need the UI in place. The
[1:21:23] create, rename, and delete dialogues
[1:21:26] plus the editor home state. So we're
[1:21:28] keeping this prompt focused on UI only
[1:21:30] with no API calls yet. Head over into
[1:21:33] context feature specs and add a new file
[1:21:37] called 04 project dialogues. Within it,
[1:21:41] we can specify that the goal is to build
[1:21:43] the editor home screen and add the
[1:21:45] project dialogues and sidebar actions
[1:21:48] with no API calls yet. So, what does
[1:21:51] this specifically mean? Well, it means
[1:21:53] that on the homepage, we want to reuse
[1:21:56] the existing editor layout without
[1:21:58] modifying the navbar or sidebar
[1:22:00] behavior, but in the center of the page,
[1:22:02] we want to add a heading, create a
[1:22:04] project or open up an existing one, and
[1:22:07] a description. Start a new architecture
[1:22:09] workspace or choose a project from the
[1:22:11] sidebar and a new project button with a
[1:22:14] plus icon. keeping the layout minimal
[1:22:17] without wrapping this content in cards.
[1:22:19] And then clicking new project should
[1:22:21] open up the create project dialogue. Let
[1:22:24] me actually show you what I mean by all
[1:22:26] of this by heading over to the finished
[1:22:28] version of the application and quickly
[1:22:30] signing in. Notice how right here in the
[1:22:32] middle we have some text greeting us
[1:22:34] even though the canvas is empty allowing
[1:22:37] us to create a new project which then
[1:22:39] opens up this dialogue. That's exactly
[1:22:41] what we want to achieve. So, we'll have
[1:22:43] a dialogue for creating a new project as
[1:22:46] well as for editing one and deleting it.
[1:22:50] So, let's specify these three dialogues
[1:22:52] below. We're going to have one for
[1:22:54] creating a project that takes in the
[1:22:56] project name input, the live slug
[1:22:59] preview based on the name, and preview
[1:23:01] updates as the user types. Then, the one
[1:23:04] for the rename with prefilled project
[1:23:07] name input, and the one for delete.
[1:23:09] Finally, on the sidebar, we want to add
[1:23:12] the following project item actions.
[1:23:14] Rename and delete. Show actions only for
[1:23:17] the projects that we own and hide
[1:23:20] actions for the shared or projects
[1:23:22] belonging to collaborators. And on
[1:23:24] mobile, tapping outside the sidebar
[1:23:26] closes it. And want to add some kind of
[1:23:28] a backdrop scrim. Finally, let's specify
[1:23:30] the implementation right here by telling
[1:23:33] it to create a dedicated hook to manage
[1:23:35] the dialogue state, the form state and
[1:23:38] the loading state. That way, we can
[1:23:40] reuse the functionality. And then we
[1:23:42] want to wire the editor home new project
[1:23:45] to create dialogue, the sidebar create
[1:23:48] button to create dialogue as well,
[1:23:50] sidebar rename to rename dialogue, and
[1:23:53] sidebar delete to delete dialogue. For
[1:23:55] now, we only want to use mock project
[1:23:57] data with no API calls. And to check
[1:24:01] when it is done, we need to check that
[1:24:03] sidebar actions are wired, that slug
[1:24:06] preview works, that no TypeScript errors
[1:24:08] exist, and there's also no linting
[1:24:10] errors. So, let's open up Claude code or
[1:24:14] your AI agent of choice. And then we can
[1:24:17] tell it to read this file, update the
[1:24:20] progress tracker.md to mark this as in
[1:24:23] progress, and then implement it exactly
[1:24:26] as specified. And let's run it. And in
[1:24:30] about a minute or so, feature 4 is done.
[1:24:33] Here's what's built. New file hooks use
[1:24:36] project dialogues which centralizes the
[1:24:39] dialogue type form including the name
[1:24:41] and the slug the loading state and mock
[1:24:44] data which exposes these different
[1:24:46] functions to deal with the dialogues.
[1:24:48] Then there's the dialogue component as
[1:24:50] well as within the project sidebar we
[1:24:53] also call the dialogues when needed. So
[1:24:56] let's quickly check this hooks file that
[1:24:58] it implemented. You can see that it is
[1:25:00] strictly typed right here with the
[1:25:02] project interface. the dialogue type to
[1:25:05] slug which takes in the name and turns
[1:25:07] it into a human readable ID and it even
[1:25:10] created some mock 3 projects that we can
[1:25:12] verify. It came up with a lot of
[1:25:15] different use states uh keeping track of
[1:25:17] all the projects, the dialogue type, the
[1:25:20] selected project, the name, slug and
[1:25:22] loading and all of these are going to be
[1:25:25] used within the dialogues themselves.
[1:25:27] Then it returns the data so we can
[1:25:29] actually use them. Let's check where the
[1:25:31] dialogue is being used. Most often it is
[1:25:33] right here within project dialogues
[1:25:36] where we have the actual code for how
[1:25:38] the dialogue looks like. If the dialogue
[1:25:40] is of a type create, then we show this
[1:25:42] one. If it's of a type of rename, we
[1:25:44] show this one. And if it's delete, we
[1:25:47] show the one below. Before we test it
[1:25:49] out, let's check out the progress
[1:25:50] tracker that says that the current phase
[1:25:52] is the feature 4 dialogues.
[1:25:55] It has the goal to do it. And it has
[1:25:58] actually completed the project dialogues
[1:26:00] with all of these different components.
[1:26:02] So now, if you come back to the editor,
[1:26:04] this is going to look much better. It's
[1:26:06] no longer just a blank screen, but
[1:26:08] rather in the middle it says create a
[1:26:10] project or open up an existing one.
[1:26:12] start a new architecture workspace or
[1:26:14] choose a project from the sidebar. And
[1:26:16] if you click create project, it actually
[1:26:19] opens up a new project dialogue where
[1:26:22] you can type something like my project.
[1:26:26] It automatically creates a slug at the
[1:26:28] bottom as well. And if you click create,
[1:26:30] you saw that creating loading. And of
[1:26:34] course, the data is currently static,
[1:26:36] but you can see how it's going to look
[1:26:37] once it actually picks the data from the
[1:26:40] database. So we have ghost AI core which
[1:26:43] you can select to edit its name as well
[1:26:48] as to delete it. This means that the UI
[1:26:51] for all of the dialogue functionalities
[1:26:53] has now been implemented alongside this
[1:26:55] centerpiece of the application. Which
[1:26:57] means that now that the majority of the
[1:26:59] UI is done in the next lesson we can
[1:27:02] start focusing on implementing real data
[1:27:04] with a real database to make our app
[1:27:07] come to life. But before we dive into
[1:27:09] the database, let's make sure that our
[1:27:11] current code is good. And I want to show
[1:27:13] you another Code Rabbit feature allowing
[1:27:15] you to review your code directly within
[1:27:18] your VS Code, which means that you don't
[1:27:20] even have to create a PR and you can be
[1:27:22] that much faster. You can install the
[1:27:24] Code Rabbit extension, authenticate to
[1:27:26] your account. It'll notice the changes
[1:27:29] that you have right now. So you can just
[1:27:31] click review all changes and the review
[1:27:33] will start directly within your editor.
[1:27:37] So, let's give it a minute. We'll check
[1:27:39] the changes and if they're good, push
[1:27:41] them. If not, we're going to fix them.
[1:27:43] And within a minute, the review is in
[1:27:45] and Code Rabbit left the comments
[1:27:47] directly on our codebase. So, you can
[1:27:50] expand all the files and click on them
[1:27:52] to see exactly what's happening. For
[1:27:55] example, right here, specify
[1:27:57] confirmation message and project name
[1:27:59] display. The delete project dialogue
[1:28:01] lacks key detail. What text should be
[1:28:03] shown to the user? Should the dialogue
[1:28:05] show which project is being deleted? And
[1:28:08] should we show the cancel button as
[1:28:10] well? These are some important
[1:28:11] questions. And it's good because in this
[1:28:13] case, Code Rabbit is telling us that we
[1:28:15] can be even more precise with our
[1:28:17] feature specifications. But let's see if
[1:28:19] it has any comments within our codebase.
[1:28:21] It says right here that the project
[1:28:23] item, that is this one right here,
[1:28:25] appears clickable, but it lacks
[1:28:28] interaction handling. It has a cursor
[1:28:30] pointer. That is this one right here in
[1:28:32] the sidebar. But when I click on it, it
[1:28:34] doesn't do anything. That's fine for now
[1:28:36] because later on we're going to make it
[1:28:38] open the actual canvas of that project.
[1:28:40] Since that is not implemented yet,
[1:28:42] that's totally fine. Then another
[1:28:44] inconsistency. Feature 4 is being marked
[1:28:47] as both in the current phase as well as
[1:28:50] finished right here at the bottom. So we
[1:28:51] need to modify the progress tracker to
[1:28:53] say that the feature five is to be done
[1:28:56] and then and then modify the current
[1:28:59] goal to be determined for feature 5.
[1:29:01] Next up feature five. This is good. And
[1:29:04] finally in the use project dialogue
[1:29:06] hooks we have a couple of comments as
[1:29:09] well. First we have missing validation
[1:29:11] for empty slug edge case. If the user
[1:29:15] enters a name containing only special
[1:29:17] characters, it passes the truthy check
[1:29:19] but returns an empty string resulting in
[1:29:22] a project with an empty slug. So if I
[1:29:24] head back right here and try to create
[1:29:26] something, take a look. It's true. I can
[1:29:29] actually create a new project, but
[1:29:32] nothing gets added to the slug because
[1:29:33] these are not valid slug characters. So
[1:29:36] we definitely have to fix this.
[1:29:38] Thankfully, what we need to do is add
[1:29:40] slug validation. So I'll just press
[1:29:43] accept right here and it'll update the
[1:29:46] code for me. That's another perk of
[1:29:48] using code rabbit within VS Code. And I
[1:29:50] think there is one other comment right
[1:29:52] here in this dialogue which is the same
[1:29:54] issue right here. Same as before, the
[1:29:57] rename operation has the edge case where
[1:29:59] the slug could end up empty. So we
[1:30:02] definitely want to fix the validation
[1:30:03] there as well. Now we can push the
[1:30:06] changes by saying get add dot git
[1:30:09] commit-m
[1:30:12] implement dialogues
[1:30:14] and then get pull to pull the latest
[1:30:16] changes and then run git push-force
[1:30:20] to push the latest changes because
[1:30:22] remember we deleted that file directly
[1:30:24] on GitHub but still we want to push the
[1:30:26] local changes as well. So now if you
[1:30:28] want to you can manually open up a PR by
[1:30:31] heading over to new pull request from
[1:30:33] the development branch over to the main
[1:30:36] branch and we can immediately merge it
[1:30:39] because we've already reviewed all the
[1:30:40] changes with code rabbit with their VS
[1:30:43] code extension. So back within the
[1:30:45] application you can run gitpool
[1:30:48] and you can also check out to main and
[1:30:50] run gitpool there as well to be up to
[1:30:53] date. But make sure to switch back to
[1:30:55] the development branch because that is
[1:30:57] where we're actively developing new
[1:30:59] features.
[1:31:02] Now that our project management UI is
[1:31:04] wired up, we need the actual database
[1:31:07] behind it. And for that we're going to
[1:31:08] use Prisma with Postgress. If you prefer
[1:31:12] a different database, the process is the
[1:31:14] same. Just swap the provider in the
[1:31:16] schema. Prisma supports Postgress,
[1:31:18] MySQL, SQLite, and more. So let's start
[1:31:22] with a manual installation right here
[1:31:24] within the terminal. Stop the app from
[1:31:26] running and then run mpm install prisma
[1:31:30] tsx at types/pg-save-dev.
[1:31:34] These are the dev dependencies so we
[1:31:37] have a nice development workflow. After
[1:31:39] that is done, you can install all the
[1:31:41] necessary packages needed for us to set
[1:31:43] up our database such as add
[1:31:45] prisma/client
[1:31:47] prisma adapter pgenv
[1:31:50] and pg itself and press enter. After
[1:31:53] that is done, initialize prisma with the
[1:31:56] correct output path for the nextgs
[1:31:58] router. You can do that by running mpx
[1:32:01] prisma init-out/app
[1:32:04] generated prisma. This creates a new
[1:32:07] Prisma folder with the schema.prisma
[1:32:10] file and an env file at the root. So
[1:32:13] head over to the Prisma dashboard. I'll
[1:32:15] leave the link down in the description
[1:32:17] and create a new account. You can sign
[1:32:19] in with GitHub or Google. And once
[1:32:22] you're in, you can create a new project.
[1:32:25] I'll call it Ghost AI. And they'll give
[1:32:28] you a one command setup. But in this
[1:32:30] case, we can proceed with the connection
[1:32:32] string. So you can just copy it and then
[1:32:35] head over into yourv and override the
[1:32:38] current database URL with the new one
[1:32:40] that you just got from the dashboard. As
[1:32:42] a matter of fact, we can take this
[1:32:43] database URL and put it within thev
[1:32:46] local as that's what we're using for our
[1:32:48] environment variables. Then open up your
[1:32:50] prisma.config.ts
[1:32:53] and update the path to the schema. It's
[1:32:55] just going to be prisma slash. We want
[1:32:58] to remove this schema.prisma Prisma
[1:33:00] because we'll make a separate Prisma
[1:33:02] model. So just use Prisma forward slash.
[1:33:05] Now before we run our spec, let's also
[1:33:08] install Prisma agent skill. We did the
[1:33:11] same thing with Clerk. So the same idea
[1:33:13] applies just for a different library.
[1:33:16] Open up your terminal and run MPX skills
[1:33:19] add Prisma skills.
[1:33:22] It'll ask you which ones you
[1:33:24] specifically want to install. And in
[1:33:26] this case, you can select all of them.
[1:33:28] CLI client API database setup Postgress
[1:33:31] Postgress setup and upgrade v7 and press
[1:33:33] enter. You can install them for cloud
[1:33:36] code within this project with sim link
[1:33:40] and we can proceed with installation.
[1:33:42] And now we are ready to generate our
[1:33:44] schemas. So let's create a new file
[1:33:47] right here within our context feature
[1:33:50] specs05-prisma.md.
[1:33:54] and one sentence update is that Prisma
[1:33:56] is already installed but we needed to
[1:33:59] add the project data models Prisma
[1:34:01] client singleton and the first
[1:34:03] migration. So then we have to start
[1:34:05] specifying the models that we want to
[1:34:07] install
[1:34:09] that we want to set up. First we're
[1:34:11] going to have the project model. So
[1:34:15] we'll ask it to add project that has to
[1:34:19] have an owner ID mapped to the clerk
[1:34:21] user a name an optional description a
[1:34:25] status enum either draft or archived a
[1:34:28] canvas JSON path for future canvas blob
[1:34:31] storage timestamps and indexes on owner
[1:34:34] ID and creation date so we can actually
[1:34:37] search through them. The second model we
[1:34:39] want to have is going to be the project
[1:34:41] collaborator which is a project relation
[1:34:44] with cascading delete. It includes
[1:34:46] collaborator email timestamp and some
[1:34:50] constraints on the project and email and
[1:34:52] indexes so we can actually map over it.
[1:34:55] Do not add any extra fields unless
[1:34:57] required by Prisma. Finally, to be able
[1:34:59] to use these models, we have to set up
[1:35:02] Prisma client. So create a lib prisma.ts
[1:35:06] ts file as a cached singleton branch by
[1:35:09] database URL. If it starts with prisma
[1:35:12] plus posgress then use accelerate else
[1:35:15] direct to add prisma adapter pg. In our
[1:35:18] case, it's going to start with posgress
[1:35:22] slash which means that it is actually
[1:35:23] hosted somewhere. Finally, we want to
[1:35:26] ask it to run the migrations and
[1:35:28] generate that Prisma client. And we want
[1:35:30] to verify whether it has installed all
[1:35:32] the dependencies such as Prisma, Prisma
[1:35:35] client, Prisma adapter PG and PG itself.
[1:35:38] And some checks are whether schema has
[1:35:41] both models with correct relations and
[1:35:43] indexes. The lib Prisma file exports one
[1:35:46] cache Prisma instance. The migration
[1:35:49] runs successfully and the mpm run build
[1:35:52] passes. So let's open up cloud code,
[1:35:54] give it this file, and tell it to read
[1:35:57] this file, update the progress tracker,
[1:36:00] and implement it exactly as specified. I
[1:36:03] think you get the idea with these
[1:36:05] prompts. The actual spec file is doing
[1:36:08] the heavy lifting. So let's see how it
[1:36:10] approaches it. It'll first read the
[1:36:12] Prisma spec, the progress tracker, the
[1:36:15] architecture context, and only then will
[1:36:18] it start implementing it. It'll first
[1:36:20] verify we have all the necessary
[1:36:22] packages and it might even consult the
[1:36:25] Prisma skill so the agent does a better
[1:36:28] way implementing the best practices. So
[1:36:30] let's give it some time and I'll be
[1:36:32] right back. Now it's in the process of
[1:36:34] creating the Prisma models for the
[1:36:36] project and the project collaborator
[1:36:39] then creating the Prisma singleton so we
[1:36:41] can actually have the client and run it.
[1:36:43] It's asking us whether we can actually
[1:36:45] run Prisma migrate. So I'll allow it to
[1:36:48] run it.
[1:36:49] and then it'll verify everything is done
[1:36:52] and we'll be able to check it all out.
[1:36:54] You can see that we have many files
[1:36:56] changed but once again the majority of
[1:36:58] these are coming from the agents that we
[1:37:00] installed or the agent skills. The
[1:37:02] actual generated files that we care
[1:37:04] about are going to be within just a
[1:37:06] couple of files such as this Prisma
[1:37:08] model right here and this Prisma client.
[1:37:12] That's it. But okay, let's let it do its
[1:37:14] thing and the feature 5 is done. Here's
[1:37:17] what's created. just two files that we
[1:37:20] need to take a look at. The first one is
[1:37:22] the project model and the second one is
[1:37:25] the Prisma client. So let's go ahead and
[1:37:27] check them out. I'll first open up the
[1:37:30] model that is going to be within models
[1:37:33] project.prisma. And it looks like I'm
[1:37:35] missing the Prisma syntax highlighting.
[1:37:38] So I'll head over into extensions and
[1:37:40] install Prisma, which should add the
[1:37:42] syntax highlighting, formatting,
[1:37:44] autocomp completion, and more. There we
[1:37:46] go. This now looks better. But yeah,
[1:37:48] essentially we have created a new model
[1:37:50] for the project with the ID, owner ID,
[1:37:54] name, description, status, the canvas
[1:37:56] which is going to be attached to a
[1:37:58] project very soon and a potential list
[1:38:00] of collaborators. And we also made it
[1:38:03] indexable so we can search for these
[1:38:04] projects. Same thing happens with the
[1:38:07] project collaborator. That's going to be
[1:38:09] a clerk ID connected to it and it's
[1:38:12] going to have access to one or more
[1:38:14] projects.
[1:38:15] Then if we take a look at the actual
[1:38:18] Prisma client that's going to be within
[1:38:20] lib Prisma, we're just using the Prisma.
[1:38:23] PG adapter to create a new Prisma client
[1:38:27] and connect it to it. Then we export
[1:38:30] this global Prisma instance that we can
[1:38:32] use to make any kind of database calls.
[1:38:35] We can't really test a lot of stuff
[1:38:37] right here because we've just built a
[1:38:38] database. But in the next lesson, we can
[1:38:41] build a couple of API routes that'll
[1:38:43] bring us one step closer to actually
[1:38:45] making use of this data. So for time
[1:38:48] being, let's just run git add dot getit
[1:38:51] commit-m
[1:38:53] implement prisma and then get push.
[1:39:00] Now that our schema is ready, we're
[1:39:02] ready to build the API routes that sit
[1:39:05] on top of it. This is backend only.
[1:39:08] We're not yet wiring the UI. That'll
[1:39:11] come next. But right now, we need to
[1:39:13] focus on one single thing. A clean,
[1:39:17] secure set of routes for creating,
[1:39:19] listing, renaming, and deleting
[1:39:22] projects. So, create a new spec right
[1:39:26] here under context feature specs 06
[1:39:30] project APIs.md.
[1:39:33] And within it, we want to tell it that
[1:39:35] the database schema is ready. So we need
[1:39:38] to build the backend project API routes.
[1:39:41] The routes are as follows. The rest
[1:39:44] endpoints for get API project which is
[1:39:47] going to list the current users
[1:39:48] projects. The post for API projects
[1:39:52] which creates a project. We have the
[1:39:54] patch for renaming and delete for
[1:39:57] obviously deleting. We can also give it
[1:40:00] a couple of rules such as use the
[1:40:03] authenticated clerk user ID as an owner
[1:40:06] ID and when creating default missing
[1:40:10] project to untitled project and use the
[1:40:13] schema's existing ID strategy without
[1:40:15] adding sequential IDs. We also want to
[1:40:18] tighten up the security a bit by telling
[1:40:20] it that the unauthenticated requests
[1:40:23] return 401 and only the project owner
[1:40:26] can rename or delete. Non-owners
[1:40:28] mutations return 40 or three. Which
[1:40:31] means that we're making our app secure
[1:40:32] not only on the client side, but the
[1:40:35] server side API calls are also going to
[1:40:37] return invalid responses if somebody
[1:40:40] tries to break them. And again, we're
[1:40:42] not yet wiring any UI. And finally to
[1:40:45] verify we need to check whether the
[1:40:47] routes exist, whether the owner checks
[1:40:50] are enforced, whether 401 and 403
[1:40:52] responses are handled correctly, and
[1:40:54] that the mpm rundev build passes. You
[1:40:57] know the drill. Open up cloud code, tell
[1:41:00] it to read the file and execute.
[1:41:03] Read this file, update the progress
[1:41:05] tracker, and implement it exactly as
[1:41:07] specified. Let's see how it does.
[1:41:10] The process of actually creating four
[1:41:13] REST API routes would take us some time
[1:41:16] and you most likely already know how to
[1:41:18] do that. But our agent is just going to
[1:41:20] do it much more quickly for us. And then
[1:41:22] when you take a look at it, you can
[1:41:23] fully understand the structure and
[1:41:25] you'll be able to add any other
[1:41:26] additional routes very easily because
[1:41:28] it's mostly boilerplate. So let's give
[1:41:30] it some time and I'll be right back.
[1:41:32] There we go. That was quick. Four routes
[1:41:35] have been created and the build is
[1:41:37] clean. All of them are right here within
[1:41:40] project routes or project project ID
[1:41:44] route. So these are the general ones and
[1:41:46] these are the ones for update and
[1:41:48] delete. Let's go ahead and check them
[1:41:50] out. They are right here under app API
[1:41:55] route.ts for general project routes
[1:41:58] where we have a asynchronous get
[1:42:00] function where we first get the user ID
[1:42:03] from O belonging to clerk.
[1:42:06] We check whether the user ID doesn't
[1:42:07] exist. In that case, we return a 401.
[1:42:11] But if it does exist, we try to find all
[1:42:13] the projects that match with that user
[1:42:16] and then we return them. Similarly, if
[1:42:18] the user is trying to create a post, we
[1:42:21] get all the data from request.json, we
[1:42:24] take the name and finally create it.
[1:42:27] Then if we want to update or delete
[1:42:29] them, you can head over to the project
[1:42:31] ID route where we can patch it based on
[1:42:34] the project ID. So we first check
[1:42:37] whether the user has access. If they do,
[1:42:40] we take a look at the context params,
[1:42:42] find the project, parse the data, update
[1:42:46] the project data, and then return it.
[1:42:48] And the same thing goes with the delete.
[1:42:50] It's going to be even simpler. We find
[1:42:52] it, we delete it, and we call it a day.
[1:42:55] It's even returning a proper 204 status
[1:42:58] which means deleted. But now in the same
[1:43:00] lesson, I want to actually create an
[1:43:03] additional feature spec which is going
[1:43:04] to be 07
[1:43:07] wire editor home.md
[1:43:10] where we want to wire the editor home
[1:43:14] sidebar and dialogues to the real
[1:43:16] project APIs we just created. So first
[1:43:20] we got to deal with data fetching
[1:43:22] because the editor homepage is a server
[1:43:25] component. So we need to fetch owned and
[1:43:28] shared projects server side using the
[1:43:31] existing project data helper and pass
[1:43:33] both lists to the sidebar and I don't
[1:43:36] want to see any client side fetching for
[1:43:38] the initial load. Now we can do that by
[1:43:41] using the project actions. So I want to
[1:43:44] create a new hook in the hooks folder
[1:43:46] that manages dialogue state and project
[1:43:49] mutation. That's going to look something
[1:43:52] like this. Create manage create dialogue
[1:43:55] state manage project name input.
[1:43:58] Generate a short unique suffix slugify
[1:44:01] the name. Call the post API projects and
[1:44:05] then navigate over to the new workspace.
[1:44:07] The project ID and livelocks room ID
[1:44:10] should stay aligned. And we can do a
[1:44:12] similar thing for rename and delete. The
[1:44:15] rename simply has to store the target
[1:44:17] project ID plus current name and then
[1:44:20] patch the name and delete has to store
[1:44:22] the target project ID and then patch it.
[1:44:25] Finally, we are ready to wire it all
[1:44:27] together by connecting the hook to the
[1:44:30] sidebar and dialogues. Create dialogue
[1:44:32] will show a room ID preview. Rename
[1:44:36] dialogue will prefill the current name
[1:44:38] and delete dialogue will show the
[1:44:40] project name. As usual, we want to run
[1:44:42] some checks when we are done and that is
[1:44:44] to see whether the sidebar uses real
[1:44:46] project data, not the fake dummy data
[1:44:48] uses right now, whether the create
[1:44:50] actually navigates to the workspace,
[1:44:53] whether the rename updates correctly,
[1:44:55] and whether delete refreshes or
[1:44:57] redirects correctly. Finally, the build
[1:45:00] has to pass. So this is the moment that
[1:45:02] our sidebar goes from mock data to real
[1:45:05] data. So let's open up our agent,
[1:45:09] tell it to read the file, update the
[1:45:12] progress tracker, and implement it
[1:45:15] exactly as specified. So let's let it do
[1:45:17] its thing and once it's done, we can
[1:45:19] test it out in the browser. And after
[1:45:22] some time, we are back. The build passes
[1:45:24] clean, and it created a couple of new
[1:45:27] files. The lib projects is used for
[1:45:30] fetching the own projects and shared
[1:45:32] projects. We can quickly check that out
[1:45:34] right here under lib projects. And you
[1:45:38] can see that this file simply exports
[1:45:41] one function called get projects for
[1:45:43] user which calls all the projects where
[1:45:46] the owner ID is the user ID that is
[1:45:49] currently signed in and then it returns
[1:45:51] all the owned and shared projects. It
[1:45:53] also created a hook that deals with all
[1:45:55] the project actions and modified some
[1:45:58] additional files such as the editor, the
[1:46:01] project's route, and some more types and
[1:46:03] props updates over the sidebar and the
[1:46:06] dialogues. So, don't forget to rerun
[1:46:08] your application by running mpm rundev.
[1:46:10] And then back on localhost 3000, we are
[1:46:13] ready to test it out by creating a new
[1:46:16] project. I'll give it a name such as my
[1:46:19] system design.
[1:46:22] And you can see that it's going to give
[1:46:24] it an additional slug right here. And we
[1:46:26] can click create project. It's creating
[1:46:29] it. And we get redirected to editor my
[1:46:33] system design. So the redirect is
[1:46:35] actually working, but there's no route
[1:46:37] under that page. But that's to be
[1:46:39] expected because so far we just wanted
[1:46:41] to test whether we can wire the database
[1:46:43] functions with the API routes. So, if I
[1:46:46] head back over to the editor and then
[1:46:48] open up the sidebar, you'll see that
[1:46:50] there's a new my system design project.
[1:46:53] And you can also rename it to something
[1:46:56] like ghost AI system architecture. And
[1:47:00] you can see that it updates it in real
[1:47:02] time or you can also just delete it.
[1:47:04] Let's test it out. Yep, that works. And
[1:47:07] it updates in real time. So this means
[1:47:09] that we have not only implemented the
[1:47:12] dialogues to create all of this but also
[1:47:15] implemented the API routes that handle
[1:47:17] the functionality. And if you're
[1:47:19] wondering why we didn't do all of this
[1:47:21] in a single prompt, well the API routes
[1:47:24] touch the backend layer and the UI
[1:47:27] wiring touches the front end and server
[1:47:29] components. Combining them gives the
[1:47:31] agent too much surface area to make
[1:47:34] assumptions across. Instead, we had two
[1:47:37] focused prompts, which means that we got
[1:47:39] back two clean results without messing
[1:47:42] up stuff on front end and the back end.
[1:47:44] So, before we go ahead and review these
[1:47:46] changes, head over to GitHub and merge
[1:47:48] the previous PR which contained
[1:47:50] implementing Prisma and even more
[1:47:52] importantly adding all of those
[1:47:54] additional files for agent skills. So,
[1:47:57] I'll just go ahead and merge it. So, now
[1:48:00] when we push this over to GitHub, we'll
[1:48:02] be able to review just those changes. So
[1:48:04] run git add dot git commit-m
[1:48:08] wire up prisma
[1:48:11] ui and rest apis
[1:48:14] and run git push. You can head over to
[1:48:16] your repo, open up a new pull request
[1:48:19] and do it specifically from the
[1:48:20] development branch. This one will be
[1:48:22] fairly quick as there's only 11 files
[1:48:24] changed. So let's give the doctor code
[1:48:27] rabbit some time to review it. In this
[1:48:29] PR, we've finally introduced the REST
[1:48:32] APIs and CRUD functionalities, making
[1:48:35] our app well full stack. We've done that
[1:48:37] across all the different files. And I
[1:48:40] always like when Code Rabbit thinks the
[1:48:42] functionality is so detailed that it
[1:48:45] actually gives us a diagram that we can
[1:48:46] review. So, as the user clicks the new
[1:48:49] project, the actions.open create
[1:48:52] dialogue runs. Then we initialize the
[1:48:54] dialogue and generate the room ID with
[1:48:57] the suffix. We ask the user to enter the
[1:49:00] project name and submit. After they
[1:49:02] submit, we set the loading and we then
[1:49:05] make a post request to our API projects
[1:49:08] which is our CRUD rest API route which
[1:49:11] then calls Prisma project create. As
[1:49:14] soon as the project is created in the
[1:49:15] database, we return the project data,
[1:49:18] set the loading to false, and bring it
[1:49:20] back and navigate over to the new
[1:49:22] project. It looks like we have one issue
[1:49:25] where we need to import the use project
[1:49:27] actions as a value and not as a type. So
[1:49:31] return type off requires the hook in a
[1:49:33] value space but import type is a typeon
[1:49:36] import that TypeScript erases from the
[1:49:38] value name space. So what we can do is
[1:49:41] just copy this import right here. Find
[1:49:44] where we're already importing a type
[1:49:46] specifically the use project actions.
[1:49:49] That's going to be right here. And
[1:49:50] instead of it, we can just import the
[1:49:52] use project actions without the type at
[1:49:55] the start.
[1:49:57] That way, when it's referred right here,
[1:49:59] we can say type off use project actions,
[1:50:02] which is a function that TypeScript can
[1:50:04] now actually understand. This is a
[1:50:06] pretty nice save. And there's another
[1:50:07] issue in the use project actions where
[1:50:10] we need to handle the failed mutations
[1:50:12] before closing or redirecting. So rename
[1:50:15] and delete always close the dialogue and
[1:50:18] refresh push even if the API calls fail.
[1:50:21] So a server or O error can look like a
[1:50:24] success. We need to gate those
[1:50:26] transitions on res.Kay and keep the
[1:50:28] dialogue open on failure. Thankfully
[1:50:30] there's a quick fix right here or we can
[1:50:32] copy just this part which is going to be
[1:50:34] the submit function. So copy the submit
[1:50:37] head over into the project actions or
[1:50:41] use project actions
[1:50:44] and again the these changes might be
[1:50:46] different for you as they are for me. So
[1:50:48] if you have some other issues to fix you
[1:50:50] can definitely do that. I'll remove the
[1:50:53] submit
[1:50:55] bring in the correct one. Push the
[1:50:57] changes by running git add dot git
[1:51:00] commit-m
[1:51:01] implement
[1:51:03] code rabbit suggested
[1:51:06] fixes
[1:51:07] and run get push.
[1:51:10] The changes will automatically be
[1:51:12] recognized right here. So we can go
[1:51:15] ahead and merge it and we are ready to
[1:51:17] continue.
[1:51:20] Before we build the canvas, let me
[1:51:22] quickly explain how Live Blocks works.
[1:51:24] Because once you understand it, the
[1:51:26] build order will make complete sense.
[1:51:29] Livelocks gives every project a shared
[1:51:32] realtime room. Think of it like a live
[1:51:35] session. Everyone who opens the same
[1:51:37] project connects to that room over
[1:51:39] websockets and any change one person
[1:51:42] makes instantly appears on everyone
[1:51:45] else's. that canvas state, multiple
[1:51:48] users cursors, the AI drawing nodes, all
[1:51:51] of it lives in that shared room and
[1:51:54] syncs in real time. Livelocks rooms are
[1:51:56] open by default. So technically anyone
[1:51:59] could connect if we let them. But since
[1:52:02] Ghost AI is a project-based app where
[1:52:05] only owners and collaborators should
[1:52:07] have access, we need to control who gets
[1:52:09] in with a sharing mechanism. So before
[1:52:12] liblocks connects a user to a room, it
[1:52:15] has to call authentication endpoints
[1:52:17] first and when we check whether that
[1:52:20] user belongs to a specific project only
[1:52:22] if they do we issue a token to let them
[1:52:25] in. That token endpoint is what we're
[1:52:28] building in this chapter. And for it to
[1:52:30] work the access control and the
[1:52:32] collaborator model have to exist. So
[1:52:35] we're doing it in this order. Workspace
[1:52:37] access first. So each project has a
[1:52:40] secure route only authorized users can
[1:52:42] enter. And then we'll focus on the
[1:52:44] collaborator model second so the system
[1:52:46] knows exactly who those authorized users
[1:52:49] are. Then live blocks and then the
[1:52:52] canvas. So head over into context
[1:52:55] feature specs and create a new file
[1:52:58] called 08editor-workspace-shell.md.
[1:53:03] And within it we'll explain exactly what
[1:53:06] has to happen next. So, let's go through
[1:53:08] it together. The goal of this prompt is
[1:53:10] to build the editor room ID workspace.
[1:53:14] Remember, that's that page that we got
[1:53:16] redirected to and we saw a 404. So, if I
[1:53:19] create a new spec right here and we
[1:53:22] navigate over to it, we get a 404. So,
[1:53:25] this is the page we're building. Before
[1:53:27] rendering, the unauthenticated users
[1:53:29] will be redirected to sign in. The users
[1:53:32] without project access will see the
[1:53:34] access denied and non-existent projects
[1:53:37] will also show access denied. Then we
[1:53:40] need to create that access denied
[1:53:42] component with a centered layout lock
[1:53:45] icon short message and a link back to
[1:53:47] the editor. And we can also create some
[1:53:49] helpers that are going to make it
[1:53:51] simpler for us to reuse the access
[1:53:53] functionality such as getting access to
[1:53:56] clerk's identity and checking whether
[1:53:58] they can access a specific project. When
[1:54:01] it comes to the layout, we want to build
[1:54:03] a full viewport workspace layout with a
[1:54:05] top bar showing the project name, navbar
[1:54:08] actions at the top right, the existing
[1:54:11] project sidebar on the left, the current
[1:54:14] room highlighted in the sidebar, central
[1:54:16] canvas placeholder with a dark
[1:54:18] background and a centered message, and
[1:54:19] the right sidebar placeholder for future
[1:54:22] AI chat. This is exactly how the final
[1:54:24] version of the application looks like.
[1:54:26] We have the left sidebar with the
[1:54:27] currently open project highlighted. the
[1:54:30] top bar with the icons on the right and
[1:54:32] then we have the AI chat which is going
[1:54:34] to be coming soon. The canvas area of
[1:54:37] course should fill the remaining space
[1:54:39] and in this case we want to tell it to
[1:54:41] not add any real canvas logic live
[1:54:44] blocks AI chat or sharing behavior yet.
[1:54:48] That's the keyword right here. When it's
[1:54:50] done, it should perform the following
[1:54:52] checks. So, let's open it up within our
[1:54:54] agent and tell it to read the current
[1:54:57] file, update the progress, and execute
[1:55:01] it exactly as specified. Of course, make
[1:55:04] sure that it knows what file you're
[1:55:05] talking about. Let's run it and give it
[1:55:08] some time to process it. And after a
[1:55:10] couple of minutes, it is done. I
[1:55:12] actually took Codex for a spin to see
[1:55:14] how well it can handle it. And yeah, it
[1:55:17] said that it implemented feature 8 as
[1:55:19] specified. The guarded workspace route
[1:55:21] now lives under this page, stays server
[1:55:24] side, and redirects unauthenticated
[1:55:26] users to sign in. The workspace shell
[1:55:28] component is right here, and it includes
[1:55:31] a project aware topn navbar with buttons
[1:55:34] to share. Okay, so let's go ahead and
[1:55:36] test it. Oh, this is looking nice. It is
[1:55:39] a bit different from the final design,
[1:55:41] but I actually love it. You can see how
[1:55:43] the sidebar collapses and then the
[1:55:45] central part actually expands. Later on,
[1:55:48] we can play a bit more with the design,
[1:55:49] but so far I love it. So, right now, we
[1:55:52] are looking the details of the new spec
[1:55:54] project because you can see that we're
[1:55:56] on that specific URL. And if you just
[1:55:58] head over to the editor, you'll be able
[1:56:00] to see something like this. You can
[1:56:02] expand the sidebar and then navigate
[1:56:04] over to the details page. If the
[1:56:06] redirect isn't working for whatever
[1:56:08] reason, send a small corrective prompt
[1:56:11] describing exactly what's happening and
[1:56:13] it'll fix it. Now, let's test access
[1:56:16] control. Open up an incognito tab and
[1:56:19] then head over to the same URL. You'll
[1:56:21] automatically be redirected back to sign
[1:56:23] in which is the first good sign. Go
[1:56:26] ahead and create a new account. I'll try
[1:56:28] to use the email and password this time.
[1:56:31] Let's go with contact JSMy Pro and a
[1:56:34] password. And it's good to see that
[1:56:36] clerk is trying to keep us safe. So,
[1:56:38] it's suggesting a stronger password. So,
[1:56:40] let me do that. There we go. And for the
[1:56:44] email, I'll use a secondary email that I
[1:56:47] have because the first one is already
[1:56:49] tied with GitHub. There we go. And we're
[1:56:51] going to even have the email
[1:56:53] verification. So, you're going to get an
[1:56:55] email that looks something like this. Go
[1:56:57] ahead and copy the verification code.
[1:56:59] Then paste it right here. And you'll be
[1:57:01] logged in and redirected to the editor.
[1:57:04] So, if once again you try to go to that
[1:57:06] same project URL,
[1:57:09] you should hit the access denied screen.
[1:57:11] you don't have access to this workspace,
[1:57:13] head back to your editor home to open up
[1:57:15] a project you actually can access.
[1:57:17] That's great. So now let's allow this
[1:57:19] user to actually invite that
[1:57:22] collaborator. To do that, I'll head over
[1:57:24] within our context feature specs and
[1:57:27] create a new file called 09 share
[1:57:31] dialogue.md.
[1:57:33] Let's go through it together. In this
[1:57:34] case, we're basically working on the
[1:57:36] share button. It's going to be within
[1:57:38] the editor navbar and it's going to open
[1:57:40] up the share dialogue allowing owners to
[1:57:44] invite collaborators by email. View
[1:57:46] current collaborators, remove
[1:57:48] collaborators, and copy the project link
[1:57:51] with the temporary copied feedback.
[1:57:54] Collaborators can view the collaborator
[1:57:56] list only and not invite, remove, or
[1:57:59] manage access. It's also important that
[1:58:01] we're going to use clerk data for the
[1:58:03] collaborator sharing system. So, they're
[1:58:05] going to be stored by email in the
[1:58:07] database and we'll use clerk's backend
[1:58:10] API to enrich the collaborator email
[1:58:12] with display name and avatar image. And
[1:58:16] if a clerk user is not found for an
[1:58:18] email, then we can fall back to showing
[1:58:20] the email only. We want to add the
[1:58:22] required API logic for listing,
[1:58:24] inviting, and removing collaborators.
[1:58:27] And we want to enforce ownership server
[1:58:29] side, not client side, for inviting and
[1:58:32] removing actions. Finally, we have a
[1:58:34] couple of checks to see whether
[1:58:36] everything's been done properly. So once
[1:58:38] again, let's open up Codex or whichever
[1:58:40] agent you're using and tell it to read
[1:58:43] the 09 share dialogue,
[1:58:47] update the progress tracker and
[1:58:50] implement it exactly as specified. We
[1:58:52] can do it within the same chat because
[1:58:55] this is somewhat related to the
[1:58:56] functionality we just worked on. Let's
[1:58:58] give it some time and I'll be right
[1:59:00] back. And in about 5 minutes, feature
[1:59:02] number nine got implemented exactly
[1:59:05] within the specs scope. The workspace
[1:59:08] navbar share button now opens a new
[1:59:10] dialogue. So what do you say that we
[1:59:13] actually test it out? Back within the
[1:59:15] browser, but not the anonymous one,
[1:59:17] which doesn't have the access, we have
[1:59:18] to go to the one that is the owner of
[1:59:21] this workspace. We can now click this
[1:59:23] share button, which allows us to copy
[1:59:25] the workspace link or invite them via
[1:59:27] email. And I love this share interface.
[1:59:30] So, I'll enter the email of my second
[1:59:32] account and click invite. You can see
[1:59:36] that the user has been invited as the
[1:59:37] collaborator. And since we signed up via
[1:59:40] email, this user doesn't have a profile
[1:59:42] photo. So now, if you head back and
[1:59:44] reload,
[1:59:47] check this out. The user now has access.
[1:59:50] And for this user, it's not under my
[1:59:52] projects, but under shared projects. And
[1:59:54] this user doesn't have the permissions
[1:59:56] to update, rename, or delete. Whereas
[1:59:59] for this user, you can see that it's
[2:00:01] under my projects and we have full
[2:00:03] permissions. That's the full
[2:00:05] collaborator flow working end to end. On
[2:00:08] our invites, collaborator receives the
[2:00:10] invites and nobody else can access it.
[2:00:13] And before we push the changes, let's
[2:00:15] review them with code rabbit. This time
[2:00:17] I'll do it directly within VS Code
[2:00:19] through the code rabbit extension. And
[2:00:22] as soon as the comments are in, we can
[2:00:23] go ahead and check them out within the
[2:00:25] use project share.ts file. That is the
[2:00:29] hook that the share button borrows the
[2:00:31] functionality from. And right here where
[2:00:34] we have the copy link button, this does
[2:00:36] nothing else than basically copy the URL
[2:00:38] to clipboard. But currently the copy
[2:00:41] link doesn't handle the clipboard API
[2:00:43] failures and the timer lacks cleanup. So
[2:00:46] if the clipboard fails due to
[2:00:48] permissions or something else, the set
[2:00:50] timeout will still fire letting the user
[2:00:52] know that it has been copied. Whereas
[2:00:54] that's not really true. So we have to
[2:00:57] set the error in case something goes
[2:00:59] wrong. We can very easily do that. I'll
[2:01:02] just copy this part right here with a
[2:01:05] try and catch block. And we have to
[2:01:07] replace everything from await navigator.
[2:01:10] So right here, await navigator. Replace
[2:01:13] it with this part right here. And we
[2:01:16] have to remove these plus signs right
[2:01:18] here at the start. Okay, great. So this
[2:01:20] one has been fixed. And I believe
[2:01:22] there's another one right here where we
[2:01:24] have the reload functionality. Reload
[2:01:27] silently swallows errors which may cause
[2:01:30] stale UI state. If the reload function
[2:01:32] fails due to a network error, the error
[2:01:35] is not captured and the UI may show
[2:01:37] outdated collaborator data after a
[2:01:39] successful invite or remove. Which means
[2:01:42] that here we also have to check for
[2:01:44] errors and display them if there are
[2:01:46] any. So once again, I'll copy this part
[2:01:48] and replace the old one. And don't
[2:01:51] forget to remove the plus signs just to
[2:01:54] make sure it works. Wonderful. So two
[2:01:56] comments in this file resolved. We have
[2:01:58] one more in the project share dialogue.
[2:02:01] This is the actual dialogue where we
[2:02:04] have a key collision when collaborators
[2:02:06] share the same email or display name.
[2:02:09] Well, that's not really going to happen,
[2:02:10] right? Because each one of the
[2:02:12] collaborators is unique. So this isn't
[2:02:14] unlikely but it's impossible. So yeah,
[2:02:17] this one is good. And finally, there is
[2:02:19] one more under project collaborators
[2:02:21] where it says batch emails in chunks of
[2:02:24] 500 to respect clerk's API limit. Well,
[2:02:28] yeah, here where we're getting the
[2:02:29] users. Uh we definitely don't want to
[2:02:31] fetch more than 500 users. This is great
[2:02:34] regardless of clerk's limit, but I'm
[2:02:36] glad that it caught it because you never
[2:02:38] want to fetch so many emails at the same
[2:02:40] time. So, in this case, it's not just a
[2:02:42] copy and paste, a couple of lines of
[2:02:44] code. What we can do here is use our
[2:02:48] agent to fix it. So, if you click that
[2:02:50] button, it's going to copy a little
[2:02:52] prompt and put it into the chat that's
[2:02:54] going to know exactly which part it has
[2:02:56] to fix. So, let's give it a second to
[2:02:57] read it and fix it. And it's done. The
[2:03:00] get clerk email now batches emails into
[2:03:03] chunks of 500 so that it doesn't go over
[2:03:05] the limit. But instead of doing that,
[2:03:08] what I actually want to do is never
[2:03:10] fetch more than 500. I mean, that's too
[2:03:12] much. So, I'll tell it. Instead of
[2:03:15] chunking the emails, maybe we just don't
[2:03:17] have to fetch so many. We can just fetch
[2:03:19] fewer emails. So, let's see how it
[2:03:21] handles a bit more vague response. I
[2:03:24] mean, so far it has been implementing
[2:03:26] everything so perfectly because our
[2:03:29] prompts or our specs, should I say, were
[2:03:32] so precise. So, it never had any issues.
[2:03:35] But yeah, in this case, it simplified
[2:03:37] it. It's going to call fewer emails.
[2:03:39] Good. So, we're going to keep this. And
[2:03:41] now that all the issues have been fixed,
[2:03:43] we actually fixed these two manually. We
[2:03:46] can just go ahead and push all of these
[2:03:48] changes by opening up our terminal and
[2:03:50] running get addit-m
[2:03:54] implement share functionality and get
[2:03:58] push. Perfect. Great job.
[2:04:04] Now that the access control is done and
[2:04:06] collaborators and sharing is enabled, we
[2:04:10] are ready to finally build the canvas.
[2:04:13] First, click the link down in the
[2:04:15] description and head over to Live
[2:04:17] Blocks.
[2:04:18] If you haven't already, create a new
[2:04:20] account. Create a new project, call it
[2:04:23] Ghost AI, and choose a region that is
[2:04:25] closest to you. And the environment can
[2:04:27] be set to development for now. Once the
[2:04:29] project is created, select personalized
[2:04:32] setup and multiplayer. Then select
[2:04:36] canvases as we want to focus on workflow
[2:04:38] diagrams, whiteboards, design tools, or
[2:04:41] in this case code architecture. And then
[2:04:43] for the guide, you can select React Flow
[2:04:46] with Nex.js. That's exactly what we're
[2:04:48] using. Then copy the first command that
[2:04:50] you can see right here and paste it
[2:04:52] within your terminal. You can press
[2:04:53] enter. And here we're installing a
[2:04:55] couple of things. The liblocks client is
[2:04:58] the core client that manages the
[2:05:00] websocket connection to liblocks. Then
[2:05:04] there's the liblocks react which
[2:05:06] contains the react hooks for accessing
[2:05:08] shared room state presence and storage.
[2:05:11] There's also the liblocks react UI
[2:05:13] containing the pre-built UI components.
[2:05:16] There's also liblocks react flow which
[2:05:19] is the bridge between liblocks and react
[2:05:22] flow. So canvases are synced in real
[2:05:24] time across all the connected users. And
[2:05:27] finally the XY flow is the React flow
[2:05:30] itself which handles the canvas nodes,
[2:05:33] edges and interaction. Once that is
[2:05:35] done, we can initialize the liblocks
[2:05:37] config file. So go ahead and copy this
[2:05:40] command and paste it into the terminal
[2:05:43] and press enter.
[2:05:45] This will generate a liblocks config.ts
[2:05:48] file at the root of our directory. This
[2:05:51] is where we define the TypeScript types
[2:05:53] for the shared room, what the presence
[2:05:55] will look like, what user data we want
[2:05:57] to attach to each connected session. You
[2:05:59] can think of it as the contract that
[2:06:01] describes everything shared between
[2:06:03] users in real time. And we'll configure
[2:06:06] it with AI. But before we do, let's
[2:06:09] install liblocks agent skills. Same
[2:06:12] pattern as with clerk and prisma. We
[2:06:14] want to allow our agent to be fluent in
[2:06:17] how liblocks works. So go ahead and copy
[2:06:20] this command or follow along with me and
[2:06:24] just run mpx skills add liblocks skills.
[2:06:30] Say y to updated and then select
[2:06:33] liblocks best practices and we don't
[2:06:35] need this second part. Press enter.
[2:06:38] Select claude or whichever agent you're
[2:06:40] using and install it for the project and
[2:06:43] using sim link. Perfect. This was quick.
[2:06:47] Now I want to split this specific
[2:06:49] feature implementation into three
[2:06:51] separate spec files. So let's take it
[2:06:54] step by step and I'll walk you through
[2:06:56] everything. First let's dive into
[2:06:58] feature number 10 liblocks setup. Here
[2:07:01] we want to tell it to set up the
[2:07:03] real-time collaboration infrastructure
[2:07:05] using liblocks. This file will wire up
[2:07:08] the entire collaboration infrastructure.
[2:07:11] the config file. We'll get the presence
[2:07:13] and user metadata types and then we'll
[2:07:15] create a liblocks client. Finally, we'll
[2:07:18] build the O endpoints like API liblocks
[2:07:22] o so we can verify that people can
[2:07:24] actually access the room. So go ahead
[2:07:26] and open it with either codeex or cloud
[2:07:29] code. Tell it to read this file, update
[2:07:33] the progress and execute everything as
[2:07:36] specified and press enter. Let's give it
[2:07:39] some time to do all the hard work for us
[2:07:41] while we remain the architect and
[2:07:44] monitor exactly what it is doing. And
[2:07:46] very soon feature 10 is complete. It
[2:07:49] implemented just three separate files.
[2:07:52] The liblocks config now with types for
[2:07:55] the presence and user metadata. The lib
[2:07:57] libelocks file which allows us to fetch
[2:08:00] the cached liblocks node client so we
[2:08:03] can use its instance. And we also have
[2:08:05] the function that maps out a specific
[2:08:08] user color. Most importantly, we have
[2:08:10] the post endpoint that verifies whether
[2:08:12] the user has been authenticated and
[2:08:14] whether it has access to the project. If
[2:08:17] it does, it returns all the data. And
[2:08:20] we're one step closer to testing it out.
[2:08:22] But all of these were just some
[2:08:23] functionalities that we need to use
[2:08:25] within our code, but we're not using
[2:08:27] them yet. So instead of testing at this
[2:08:29] point, what I want to do is head over to
[2:08:32] feature number 11. That's going to be
[2:08:35] the base canvas MD. So right here in
[2:08:39] lesson 11, we want to replace the canvas
[2:08:42] placeholder with a real liblocksbacked
[2:08:46] ReactFlow canvas, allowing multiple
[2:08:49] users to connect to a Liblocks room and
[2:08:53] share the same canvas state. That means
[2:08:55] that the nodes and edges will sync in
[2:08:58] real time. And after that, we can
[2:09:00] basically say that we have a full
[2:09:02] collaborative canvas application. Not
[2:09:05] yet polished, but real. We don't want to
[2:09:08] add any controls yet or custom nodes or
[2:09:11] edges. We just want to create that
[2:09:13] canvas. So, let's open this up in a new
[2:09:16] chat. As usual, I'll tell it to read the
[2:09:19] file,
[2:09:21] update the progress, and execute as
[2:09:25] specified. And I've just went to grab a
[2:09:28] coffee and feature 11 is done. So let's
[2:09:31] review it. It built out the canvas types
[2:09:34] so that our application remains heavily
[2:09:36] typed. Then it added the storage part
[2:09:39] over to the lib blocks config. This
[2:09:42] matters right here because it knows that
[2:09:43] we're going to be keeping track of the
[2:09:45] presence of the cursors and whether
[2:09:47] they're thinking, but also the storage
[2:09:49] of different nodes and edges and users
[2:09:52] on the screens. Later on, we're going to
[2:09:53] fill up these two. And finally using
[2:09:55] liblocks provider and the room provider
[2:09:58] it created the canvas room and most
[2:10:01] importantly the canvas placeholder got
[2:10:03] replaced with that room. So what do you
[2:10:06] say that we go ahead and test it out?
[2:10:08] Back on localhost 3000 we got connecting
[2:10:11] to a room but there is one issue. It
[2:10:14] says liblocks authentication failed
[2:10:17] reason not provided. Maybe because this
[2:10:19] project was created before our whole lib
[2:10:21] block setup. So, what I'll do is delete
[2:10:23] it, reload the page, and create a new
[2:10:26] project. I'll call it liblocks live
[2:10:30] room, and create. Unfortunately, we
[2:10:33] still get the same issue. Thankfully,
[2:10:35] the error in the terminal gives us a bit
[2:10:38] more info. It looks like we're missing
[2:10:39] the livelocks keys. So, if you head over
[2:10:42] to your project under API keys, you'll
[2:10:45] be able to see your public key and the
[2:10:46] secret key. So, go ahead and copy them
[2:10:49] and add them to your env.local. local
[2:10:52] where we can first specify the liblocks
[2:10:55] public key as well as the liblocks
[2:10:58] secret key. With these two keys in
[2:11:01] place, head back over to your
[2:11:03] application and reload. And after
[2:11:05] connecting to room, you'll be able to
[2:11:07] see the actual canvas. This is the
[2:11:10] ReactFlow canvas underneath that you can
[2:11:13] move through. And there's even a little
[2:11:15] window that you'll be able to scroll
[2:11:16] through to very quickly access specific
[2:11:19] parts of the workspace. This is looking
[2:11:21] absolutely amazing. We can even expand
[2:11:23] it by collapsing the left sidebar. Oh,
[2:11:26] and the right sidebar is collapsible
[2:11:28] too. So now we have a real fully
[2:11:31] functional React Flow canvas. But of
[2:11:34] course, what is the canvas for if we
[2:11:36] can't add any elements on top of it? So
[2:11:38] let's create a little bottom navigation
[2:11:41] that allows us to add some shapes that
[2:11:43] are going to act as specific parts of
[2:11:45] the diagrams within our application.
[2:11:47] We'll do that by creating a new feature
[2:11:50] spec called 12 shape panel.md.
[2:11:55] You can add it right here. This one will
[2:11:57] be simple. And what this does is it adds
[2:12:00] a floating toolbar at the bottom of the
[2:12:03] canvas where users can drag shapes onto
[2:12:06] the canvas to create nodes, rectangle,
[2:12:09] diamond shapes, circles, pills,
[2:12:11] cylinders, and hexagons for databases.
[2:12:14] And after this, users will actually be
[2:12:17] able to start creating the architectural
[2:12:20] diagrams. We want to allow the users to
[2:12:22] drag a shape including the shape name
[2:12:24] and the default size. Then they can also
[2:12:27] drag and drop it. And on drop, we need
[2:12:31] to read the dragged shape payload,
[2:12:33] convert it to the screen position,
[2:12:35] create a new node at that position, use
[2:12:38] an empty label and the default color. We
[2:12:40] then want to give each one of these
[2:12:42] shapes a node ID with their shape name,
[2:12:45] time stamp, and a counter. And we want
[2:12:48] to render it. So, this is an exciting
[2:12:51] one. So, let's get it built, read the
[2:12:53] file, update the progress, and execute
[2:12:56] it exactly as specified. I'm sure
[2:12:57] there's an easier way for me to just
[2:12:59] read the file, and not have to repeat
[2:13:02] this sentence every now and then. I
[2:13:04] mean, I could have put it at the top of
[2:13:05] that file and just shared the file
[2:13:07] itself. That would have worked. Uh, but
[2:13:09] yeah, I don't mind it. It's the actual
[2:13:12] work that you put before that saves you
[2:13:14] so much time later down the line. This
[2:13:16] one took a bit longer, but feature 12 is
[2:13:19] done. It created the canvas node
[2:13:22] renderer and a floating pill toolbar at
[2:13:24] the bottom with six dragable shapes. So,
[2:13:27] if you head back over to your room, take
[2:13:30] a look at the bottom. You have the
[2:13:32] rectangle, which you can drag and drop.
[2:13:35] Hopefully, nope. As I dropped it, it
[2:13:38] didn't appear on the screen. Let's try
[2:13:41] with a second one. It looks like I can
[2:13:44] drag and drop them, but they're not
[2:13:45] actually showing up on the screen, which
[2:13:47] makes it a great opportunity to debug it
[2:13:49] the proper way by specifying in detail
[2:13:52] the current issue that we're
[2:13:53] experiencing. So, I took a second to
[2:13:56] write all of the issues that I believe
[2:13:58] we currently have with the application,
[2:14:00] at least that I have on my version of
[2:14:02] the app. Your agent might have done
[2:14:04] something different. So, let's go
[2:14:06] through everything together first, and
[2:14:07] then you'll be able to tell your agent
[2:14:09] to fix some issues that you see on your
[2:14:11] end as well. Let's think of this as a
[2:14:13] little corrective prompt. So, review the
[2:14:16] editor canvas implementation and fix the
[2:14:18] visual issues. The canvas currently
[2:14:20] looks like it's floating above the
[2:14:22] background inside a border box instead
[2:14:25] of feeling like a real design canvas.
[2:14:27] And I want to teach you how we can also
[2:14:29] add images to the context. So right here
[2:14:31] within the context you can create a new
[2:14:34] folder called screenshots and then you
[2:14:36] can screenshot the entire design and
[2:14:39] simply drag and drop it in. Of course
[2:14:42] I'll rename it to image as I specified
[2:14:45] right here within the document. That way
[2:14:47] you can also give your agent some visual
[2:14:49] feedback.
[2:14:51] Also read the current canvas component
[2:14:53] code in the components editor. And here
[2:14:56] are a couple of issues to look for.
[2:14:57] Obviously, and first of all, the drag
[2:15:00] and drop issues, right? The canvas nodes
[2:15:03] from the node panel cannot be dragged
[2:15:05] and dropped under the canvas. We need to
[2:15:07] investigate the full drag and drop
[2:15:09] pipeline. We need to confirm that the
[2:15:11] dragable nodes in the node panel have
[2:15:13] the correct dragable attribute. That the
[2:15:16] canvas has the on drag over handler and
[2:15:19] on drop allowing us to drop them. that
[2:15:21] the drop handler reads the node type
[2:15:24] from data transfer, calculates the
[2:15:26] coordinates, and then actually creates a
[2:15:28] new node at the drop position. And while
[2:15:31] we're fixing the drag and drop issues, I
[2:15:33] also thought we can fix some uh visual
[2:15:35] inconsistencies, such as the way that
[2:15:37] the canvas and the left and the right
[2:15:39] sidebar are positioned. So the left and
[2:15:41] the right sidebar should float over the
[2:15:43] canvas, not push or shrink it. sidebars
[2:15:46] must use fixed position or absolute with
[2:15:48] a higher Z-index and so on. So after
[2:15:52] documenting all issues, we want to fix
[2:15:54] all of the above so that it basically
[2:15:56] corrects what we specified. So let's
[2:15:59] actually open this up right here. We can
[2:16:01] tell it to read this file and fix all of
[2:16:04] the listed issues and then run it. So
[2:16:08] we've done three things. First, we gave
[2:16:11] Claude code some file references up
[2:16:14] front and the screenshots right here.
[2:16:16] This stops it from wandering around the
[2:16:18] entire project trying to figure out
[2:16:20] where things live. We're pointing it
[2:16:22] exactly where to look. We're listing
[2:16:24] every issue one by one and mixing some
[2:16:27] technical hints alongside them. These
[2:16:29] technical details act as shortcuts. They
[2:16:32] give the AI the stronger starting point
[2:16:34] so it can find and fix the root cause
[2:16:37] faster instead of guessing. And third,
[2:16:39] at the bottom, we describe exactly what
[2:16:42] success looks like. The AI now knows not
[2:16:45] just what's broken, but what's done
[2:16:47] looks like. So, let's see if it can
[2:16:49] manage to correct itself and fix it
[2:16:51] quickly. After reading through some of
[2:16:53] these files, it has a full picture of
[2:16:55] all the issues. So, it's going to use
[2:16:57] the to-do write to track the fixes and
[2:17:00] then implement them. Fix the canvas
[2:17:03] layout was the first thing. removing the
[2:17:05] card styling and making it a fill full
[2:17:07] viewport. Fixing the left sidebar not
[2:17:09] fully hiding when closed. Fixing the
[2:17:12] dotted canvas background visibility. And
[2:17:14] finally, and most importantly, verifying
[2:17:16] the drag and drop pipeline. And see how
[2:17:19] well we did. Uh it's even thanking us.
[2:17:21] Uh specifying that the core issue is
[2:17:24] clear from the screenshot of the code.
[2:17:26] The canvas is boxed inside a padded main
[2:17:29] with card styling and the layout shrinks
[2:17:32] the canvas to accommodate sidebars
[2:17:34] instead of floating over them. So, it's
[2:17:36] going to fix it very easily. Perfect.
[2:17:39] Hopefully, this video is teaching you
[2:17:41] how you can approach developing apps
[2:17:43] with AI. You are the architect and agent
[2:17:47] is just a coder. And there we go. All
[2:17:50] four files have been updated. So, let's
[2:17:53] test it out. Back into the browser, I
[2:17:55] will reload. You can see that now the
[2:17:58] canvas spans across left and right and
[2:18:01] the left and right sidebar appear to be
[2:18:04] floating on top of it. So if you want to
[2:18:06] hide it, it just gets completely hidden
[2:18:08] away, which is great. And the right
[2:18:10] sidebar also gets completely hidden
[2:18:13] away. So we have a complete canvas. This
[2:18:16] is a big difference from what we had
[2:18:18] before because now if you hide the
[2:18:20] sidebars, you have so much more space to
[2:18:22] work with. And what happens if we try to
[2:18:24] drag and drop an element? It looks like
[2:18:27] that functionality is still not working
[2:18:29] properly. And I think that's because
[2:18:30] Claude focused mostly on cosmetic
[2:18:33] changes and the layout. I don't see too
[2:18:36] many mentions of the drag and drop
[2:18:38] functionality being fixed. So what we
[2:18:40] can do now is head over into the current
[2:18:43] issues and specify that we want to fix
[2:18:46] the drag and drop functionality.
[2:18:50] So, we're going to remove everything
[2:18:52] else besides the drag and drop and keep
[2:18:55] the last part saying nodes can be
[2:18:57] dragged from the node panel and dropped
[2:18:59] under the canvas correctly. So, now we
[2:19:01] can say read the current issues file
[2:19:04] again and fix the remaining issue and
[2:19:07] press enter.
[2:19:09] This time it's all about the drag and
[2:19:11] drop. And after some thinking, it looks
[2:19:14] like it found the root cause. The
[2:19:16] ReactFlow viewport has pointer events
[2:19:19] none. And React Flow internally uses D3
[2:19:22] zoom or native pointer listeners that
[2:19:25] call prevent default on pointer down. So
[2:19:28] when the shape panel is rendered inside
[2:19:30] of the React flow as a panel, those
[2:19:32] pointer handlers interfere with the
[2:19:34] browser's drag gesture recognition
[2:19:36] before dragstart can fire. The standard
[2:19:39] React Flow drag and drop pattern puts
[2:19:41] drag sources outside of the React Flow
[2:19:44] and puts onrop or on drag over on a
[2:19:46] wrapper div not on the React Flow
[2:19:48] component. So, it's going to fix this
[2:19:50] issue for both the canvas editor and the
[2:19:53] shape panel. That's it. No types of
[2:19:55] errors. The fix is clean. We specified
[2:19:57] what was wrong and the fix was to move
[2:20:00] the on drag over and on drop from the
[2:20:02] react flow component to the outer
[2:20:04] wrapper and also to replace the panel
[2:20:07] position from bottom center which is
[2:20:09] react internal panel with a plain
[2:20:11] absolutely position div. So let's test
[2:20:13] it out back on local host 3000 within a
[2:20:16] specific project. I'll drag and drop
[2:20:19] this rectangle and it still doesn't do
[2:20:21] it. So what I'm thinking is maybe we can
[2:20:24] make use of that liblocks agent skills
[2:20:26] that we installed earlier. I mean this
[2:20:29] is the exact situation they're built
[2:20:30] for. So in the same context window,
[2:20:32] let's simply tell the agent to check the
[2:20:36] lib blocks best practices and fix the
[2:20:38] drag and drop flow. Dragging shapes from
[2:20:41] the shape panel should create new nodes
[2:20:43] on the canvas, but it's still not
[2:20:46] working. Nodes should be draggable from
[2:20:48] the panel and dropped onto the canvas
[2:20:50] correctly. So by telling it to check the
[2:20:52] liblocks best practices, I'm hoping that
[2:20:55] it's going to consult the liblocks agent
[2:20:57] skill. So let's give it a shot. And you
[2:20:59] can see that that is the first thing
[2:21:00] that it did. Libbel blocks best
[2:21:02] practices. After analyzing it, it came
[2:21:04] back with the complete picture with
[2:21:06] three things that are wrong. The storage
[2:21:09] type declares stople nodes and edges,
[2:21:11] but use slime blocks flow actually
[2:21:13] stores everything under a nested flow
[2:21:16] key within the canvas room. The initial
[2:21:17] storage creates tople nodes and edges.
[2:21:20] Once again, wrong schema. And then the
[2:21:22] canvas editor add node mutation calls
[2:21:25] storage.get nodes, which writes to the
[2:21:28] wrong storage path.
[2:21:30] Instead, it should use on nodes change
[2:21:32] with a type of ad and then the item
[2:21:34] we're adding. So, let's wait until it
[2:21:37] fixes all three. And it says clean. So,
[2:21:40] let's actually test it out. Back within
[2:21:42] the browser, I'll reload the page. And
[2:21:44] I'll try drag and dropping a node once
[2:21:46] again. And you can see that this time we
[2:21:49] actually get a shape. Now, if you try
[2:21:51] drag and dropping another shape, you'll
[2:21:53] see that it'll just give you another
[2:21:55] rectangle. And yet another rectangle of
[2:21:58] a different size. You're only getting
[2:22:00] rectangles. And that's okay for now
[2:22:03] because in the next lessons, we're going
[2:22:05] to turn these rectangles into different
[2:22:07] shapes. We'll basically make it like a
[2:22:09] real architecture canvas where you can
[2:22:11] connect different nodes and give them
[2:22:13] titles and make them make sense. But
[2:22:16] thankfully, we fixed this shape drag and
[2:22:18] dropping feature, which is one of the
[2:22:19] bigger features in the app. And while
[2:22:21] fixing it, I wanted to keep the full
[2:22:23] process of me doing that. So, you're not
[2:22:26] just watching me copy and paste from the
[2:22:27] other screen. We're actually debugging
[2:22:30] this together. And in this case, the
[2:22:32] solution was to invoke an agent skill.
[2:22:35] So, whenever you're working with
[2:22:36] specific tools, always verify that they
[2:22:39] also have their agent skills, install
[2:22:41] them, and ask your agent to use them.
[2:22:44] Okay, great. So let's actually get these
[2:22:46] changes pushed by saying get add dot get
[2:22:49] commit-m
[2:22:50] implement drag and drop canvas
[2:22:54] functionality and then run get push and
[2:22:57] I'll actually open up a PR for this and
[2:22:59] get it merged so that in the next lesson
[2:23:01] we can focus on adding more canvas
[2:23:04] features. For these, we already reviewed
[2:23:06] most of the changes before, so I won't
[2:23:09] be reviewing them again. And we have to
[2:23:11] resolve the conflicts right here within
[2:23:13] our current issues. And there's a fix
[2:23:15] with copilot thing right here. Resolve
[2:23:17] the merge conflicts in this pull request
[2:23:19] by clearing the current issues.md file.
[2:23:25] We basically want to make it empty. As
[2:23:27] we said, we don't need to push whatever
[2:23:29] is in the current issues file. This is
[2:23:31] also a new feature by GitHub where the
[2:23:33] copilot can automatically fix it on our
[2:23:36] behalf. And once it does, we'll be able
[2:23:38] to merge it back to the main branch and
[2:23:40] continue developing. And there we go. It
[2:23:43] basically cleared out the file and we're
[2:23:44] good to merge it. So now back within the
[2:23:47] editor, you can just run get pull to
[2:23:49] pull the latest changes and we're ready
[2:23:51] to continue with the next feature.
[2:23:55] In this lesson, the goal is to make the
[2:23:57] canvas feel like a real product. So,
[2:24:01] open up your feature specs and go ahead
[2:24:04] and create another one that's going to
[2:24:06] be 13 node shape.md.
[2:24:09] In this lesson, we're going to actually
[2:24:11] polish and add six features. Each one
[2:24:14] will add a distinct layer of interaction
[2:24:17] so that by the end, the canvas will have
[2:24:19] proper shape rendering, node colors,
[2:24:22] edge behavior, and keyboard shortcuts.
[2:24:24] everything that makes a difference
[2:24:25] between a working prototype and
[2:24:28] something that genuinely feels polished
[2:24:30] to use. So, starting with the first one,
[2:24:33] it's going to be the node shape. It's a
[2:24:35] fairly simple one where we just want to
[2:24:37] replace the placeholder node renderer
[2:24:39] with proper shape rendering and a drag
[2:24:41] preview. So, instead of a placeholder
[2:24:44] node shape, which is just a rectangle,
[2:24:46] we want to render all of these different
[2:24:48] types of shapes through SVGs. They
[2:24:51] should scale with the node size and we
[2:24:53] want to keep the border subtle. We also
[2:24:55] want to add a shape drag preview while
[2:24:57] we're dragging. We want to keep the node
[2:25:00] rendering connected to the existing
[2:25:01] collaborative canvas state. We don't
[2:25:04] want to rebuild anything. And when we're
[2:25:07] done, we want to check that the node
[2:25:09] renderer renders the correct shape
[2:25:11] variant for each type. So, you know the
[2:25:14] drill. Open up your agent and let's ask
[2:25:16] it to read this file, update the
[2:25:19] progress and implement it as specified.
[2:25:22] Let's give it some time and I'll be
[2:25:23] right back. And a couple of minutes
[2:25:25] after feature 13 is done, it replaced
[2:25:29] the single style placeholder with a
[2:25:31] shape aware rendering and also added the
[2:25:34] cursor tracking ghost preview. I'll show
[2:25:36] you what that means quickly,
[2:25:38] but basically now you can see that our
[2:25:40] array of rectangles that we created
[2:25:42] before is now a bunch of different
[2:25:45] shapes and we can actually move across
[2:25:47] the canvas and drag and drop different
[2:25:49] shapes. There's a mini map at the bottom
[2:25:51] as well which we can later on remove as
[2:25:53] we don't need it as we'll be mostly
[2:25:55] working within a single centralized
[2:25:56] place. But yeah, we now have the shapes
[2:25:59] and you can actually connect the shapes
[2:26:01] together. But we still can't change the
[2:26:03] size of the nodes, right? They are
[2:26:06] always of the same size and we can't
[2:26:08] edit their labels. Like currently these
[2:26:10] are just shapes. They don't have any
[2:26:11] data associated with them. So what we
[2:26:14] can do is create another file right
[2:26:17] here, another feature 14 node
[2:26:21] editing.md.
[2:26:23] And within it, we essentially want to
[2:26:25] add resizing and inline label editing to
[2:26:28] the canvas. so that when we select a
[2:26:30] specific node, we can resize it and
[2:26:32] scale them however we need to. And if we
[2:26:35] doubleclick it, we'll be able to edit
[2:26:37] its label. So this is the next feature
[2:26:39] that we're going to develop. I'll tell
[2:26:40] it to read the file, update the
[2:26:43] progress, and implement it exactly as
[2:26:48] specified. And you know what? I will
[2:26:50] actually copy this part right here. So
[2:26:53] in the future, I can just paste it into
[2:26:55] the prompt. Okay. And after some wearing
[2:26:59] and coitating and thinking, let's see
[2:27:01] what it'll actually come up with. And as
[2:27:04] it's close to being done after running a
[2:27:06] couple of minutes, um near the end, uh
[2:27:10] when it tries to build and check for
[2:27:12] errors, it almost always finds some type
[2:27:15] issues. Like right here, it was
[2:27:17] complaining about the canvas node. So it
[2:27:20] expanded the types and made it a bit
[2:27:22] more type- safe. And only once that is
[2:27:24] done, it actually updates the progress
[2:27:27] tracker and then finishes with the
[2:27:28] feature. So it's always great to ask it
[2:27:30] to test the application and test the
[2:27:32] output. Okay, great. So the resizer from
[2:27:36] XY flow now renders when a node is
[2:27:38] selected and we can resize dimension
[2:27:40] changes through live's on node change
[2:27:43] automatically. Also double clicking any
[2:27:45] node opens up a text area. So let's go
[2:27:48] ahead and test it out. We now have these
[2:27:51] labels which is perfect. But first,
[2:27:54] let's test the resizing. If I now pull
[2:27:57] it at any of the borders or even at any
[2:28:01] of the edges, you can see that this is
[2:28:03] very precise and would take us some time
[2:28:05] to implement properly. You can now
[2:28:07] resize it both horizontally and
[2:28:09] vertically or if you want to keep the
[2:28:11] aspect ratio, you can resize it by the
[2:28:13] edges. This is absolutely amazing. And
[2:28:17] let's also test changing the label by
[2:28:19] double clicking right here and typing
[2:28:21] something like start of the app and
[2:28:26] leaving it. And you can see that it
[2:28:27] looks good. It quickly brings the text
[2:28:29] up in case you want to type more stuff
[2:28:31] into it. But but we can fix that later
[2:28:34] on because the text will mostly always
[2:28:37] stay centered. So if we pull some kind
[2:28:39] of a label, we can now mark this as a
[2:28:41] Postgress DB for example and it's going
[2:28:45] to fall down right here. And we can now
[2:28:47] connect the application that way.
[2:28:50] Perfect. Let's just quickly tell it that
[2:28:51] even though while we're typing into the
[2:28:53] field, we want the text to stay in the
[2:28:56] middle. Right now it jumps to the start.
[2:28:58] So, I'll take a quick screenshot while I
[2:29:01] am typing and drag and drop it into the
[2:29:04] chat and tell it while the label editing
[2:29:07] is focused, the text appears at the top
[2:29:10] of the element instead of in the middle
[2:29:12] where it falls back to when not focused
[2:29:15] any longer. Make it so that when we're
[2:29:18] typing, we're also typing within the
[2:29:20] middle of the element. Hopefully, this
[2:29:22] should be clear enough for a little
[2:29:24] quick corrective fix. And very quickly,
[2:29:26] the build passes. It just sweped the
[2:29:28] text area for the content editable div.
[2:29:31] So now if we head back right here and
[2:29:33] start typing, you can see that it
[2:29:35] remains in the middle. And you can say
[2:29:37] start here, we can say
[2:29:40] label. And as soon as we start typing,
[2:29:43] it basically centers itself right in the
[2:29:46] middle. Wonderful. So now that we can
[2:29:49] actually type within these inputs, what
[2:29:51] do you say that we implement the
[2:29:52] functionality to also be able to
[2:29:54] differentiate them by color? So create a
[2:29:57] new feature spec called 15 nodes color
[2:30:01] toolbar.m MD. And here we want to add a
[2:30:05] floating color toolbar that appears when
[2:30:08] a node is selected. We then want to
[2:30:10] allow the user to pick a color and both
[2:30:12] the node background and text color will
[2:30:15] update instantly synced across all
[2:30:18] collaborators in real time. So it'll
[2:30:20] check our UI context for the node color
[2:30:22] palette, include a background color as
[2:30:25] well as a matching text color so that
[2:30:27] the contrast is nice and we want to
[2:30:29] reuse existing colors if they exist in
[2:30:31] globals. Otherwise, it can keep the
[2:30:33] palette in the canvas types. Then we
[2:30:36] want to add a toolbar above the selected
[2:30:39] node that'll only show when the node is
[2:30:41] selected. And when a color is selected,
[2:30:45] we want to update the node background
[2:30:47] color and text color. I think this is
[2:30:49] pretty understandable. So, let's
[2:30:51] actually build it by telling it our
[2:30:54] usual secret sentence, which is super
[2:30:56] simple, but again, the spec file does
[2:30:59] the heavy lifting. This one, for some
[2:31:01] reason, was super quick. It added the
[2:31:03] text color, the ability to choose
[2:31:05] between a predefined set of colors, and
[2:31:07] also the color background. So, if we
[2:31:10] head back over here and select an
[2:31:12] element, would you look at that? I mean,
[2:31:14] this is really starting to come into
[2:31:16] life. And I'm not sure how much time
[2:31:18] this would take me to manually code it
[2:31:21] out, but this way we just have to think
[2:31:23] of an idea, write a fairly simple yet
[2:31:26] descriptive uh spec file, and then it
[2:31:29] does it instantly. And take a look, you
[2:31:33] can actually select the colors of each
[2:31:36] one of the nodes separately. So if I
[2:31:40] make this one purple, the database, for
[2:31:42] example, can be green. Uh, yep. For
[2:31:45] example, this one can be MongoDB in its
[2:31:48] classic green color. Then we can have
[2:31:50] some kind of an algorithm right here
[2:31:51] going on which can be orange. And yeah,
[2:31:55] it is all working wonderfully. So on top
[2:31:58] of the colors, what else is there to
[2:32:00] implement? Currently, there's these
[2:32:02] custom edges from all four sides. But no
[2:32:04] matter what you select, it's always
[2:32:06] going to start making a connection from
[2:32:07] the bottom as you can see right here.
[2:32:09] And it'll connect it to the bottom or
[2:32:11] the top as well. So, we want to fix that
[2:32:14] edge behavior. So, I'll create a new
[2:32:16] spec just for that. And you can see how
[2:32:18] I'm being very specific with the specs,
[2:32:21] only focusing on the smallest thing
[2:32:23] possible. So, 16 edge behavior
[2:32:28] MD. And the goal of this spec is to just
[2:32:31] replace the default canvas edges with
[2:32:34] custom edges that feel easier to follow,
[2:32:37] easier to click, and support inline
[2:32:39] labels. So, we want to add connection
[2:32:41] handles to every node at the top, right,
[2:32:44] bottom, and left sides. And users should
[2:32:46] be able to connect from any handle to
[2:32:48] any other handle. Oh, and another thing
[2:32:51] you can notice is that we're opening up
[2:32:53] a new chat for every single one of these
[2:32:56] specs. This helps us with lowering the
[2:32:59] overall context window and the amount of
[2:33:01] tokens that we are spending for each
[2:33:03] transaction. And it also makes the agent
[2:33:06] that much more focused on the task at
[2:33:08] hand. And all these little things
[2:33:10] together like the separate feature spec
[2:33:12] MD files instead of just regular
[2:33:14] messages or the current issues file
[2:33:17] where we can specify what's wrong and
[2:33:19] these six files that altogether make the
[2:33:22] system work just makes it a breeze to
[2:33:24] work with an AI which is typically not
[2:33:26] the case because it starts imagining
[2:33:28] things and creating stuff that we don't
[2:33:30] want or breaking other things. But this
[2:33:32] way it is super predictable. And if you
[2:33:35] take a look at the progress tracker,
[2:33:37] which we haven't looked at in a long
[2:33:39] time now, you'll see that everything
[2:33:42] we've done so far is written right here.
[2:33:45] But what I care more about is that it
[2:33:47] even kept some additional architectural
[2:33:49] decision so that it knows what we're
[2:33:51] doing and the session notes for
[2:33:53] specifically what it thought is very
[2:33:55] important like the specific versions of
[2:33:57] different tools that we're using. the
[2:33:59] fact that the Prisma config uses Prisma
[2:34:01] forward slash and not some other path
[2:34:04] and that it reads the database URL from
[2:34:06] the env. It kept everything it needs and
[2:34:09] everything that future sessions with AI
[2:34:11] or other developers continuing to
[2:34:13] develop this project need to do it in a
[2:34:16] sane and happy way. And another build
[2:34:19] passes. It implemented the canvas edge
[2:34:22] data pieces allowing us to connect the
[2:34:24] source and the end. So if you head back
[2:34:28] over here, you can see that we have
[2:34:29] plenty of different lines happening. But
[2:34:31] now if you select it from the left side,
[2:34:34] you can see how it creates a bit of a
[2:34:35] different kind of connection. And you
[2:34:37] can now connect it to another element.
[2:34:40] This line looks a bit different from
[2:34:42] other more organic looking lines. Oh,
[2:34:44] and right now we cannot even delete the
[2:34:46] elements. So we have plenty of elements
[2:34:48] on the screen. But I'll create a new one
[2:34:51] right here and another database on the
[2:34:53] right. drag the canvas so we can see
[2:34:56] them right here. Now the mini map starts
[2:34:58] making a bit more sense as you can see.
[2:35:00] But if you try to connect it, you can
[2:35:02] now do that in a bit of a more
[2:35:04] consistent and better way. Now that the
[2:35:07] canvas is looking so good, I guess we
[2:35:09] can focus on little quality of life
[2:35:11] fixes. Like under feature specs, we're
[2:35:13] going to do 17 canvas ergonomics.md.
[2:35:18] And within it, we can focus on adding a
[2:35:21] little floating control bar for zooming
[2:35:23] in and out and undoing or redoing and
[2:35:26] then wiring those actions to keyboard as
[2:35:28] well. So if you press plus or equal,
[2:35:30] it's going to zoom in, minus to zoom
[2:35:32] out, command or control Z or Y to undo
[2:35:36] and redo. And I also don't like that
[2:35:39] mini map at the bottom right. I don't
[2:35:41] think our app will need it. So I'll
[2:35:42] simply say remove the mini map at the
[2:35:46] bottom right. It's just a personal
[2:35:48] preference, but yeah, this is that
[2:35:50] finishing layer that makes the canvas
[2:35:52] feel like a tool that somebody would
[2:35:53] actually use every day. So, let's
[2:35:55] implement this one as well. And very
[2:35:57] quickly, feature 17 is done as well. We
[2:36:00] now have a new pillshaped floating bar
[2:36:02] at the bottom left for zooming in and
[2:36:05] out or fitting within the view. So, if
[2:36:07] we collapse the sidebars, you'll be able
[2:36:09] to see it right here at the bottom. Ooh,
[2:36:12] it it actually looks very nice. And if I
[2:36:14] move some things around, you can see
[2:36:16] that the left arrow or the undo actually
[2:36:20] starts shining and you can undo previous
[2:36:23] actions or redo them. You can also use
[2:36:25] command or control Z or Y to actually go
[2:36:29] back and forth which is absolutely
[2:36:31] amazing. There's this fit in view which
[2:36:33] is going to fit all the elements within
[2:36:35] the view. So if you're working on
[2:36:36] something that is a bit closer together,
[2:36:38] it's going to actually increase the view
[2:36:40] which is always nice. And you can zoom
[2:36:42] in or you can zoom out, but that's
[2:36:44] hidden by the Nex.js logo, but that's
[2:36:46] only in development.
[2:36:48] So these little things really do make a
[2:36:51] big difference. And finally, I had an
[2:36:53] idea that isn't even necessary, but I
[2:36:55] want to make it work. So let's create a
[2:36:58] new feature spec 18 starter template.md.
[2:37:03] The goal of this one is to create a
[2:37:05] template library that lets users start
[2:37:08] from a pre-built diagram instead of
[2:37:11] blank canvases. So we can start with
[2:37:13] some ideas like let's say microservices
[2:37:17] or a CI/CD pipeline or an event-driven
[2:37:19] system. Each one will load directly into
[2:37:22] the shared canvas. That's going to make
[2:37:24] it easier for users to figure out how to
[2:37:26] actually use the app and what are the
[2:37:28] different use cases because maybe
[2:37:30] somebody is not going to even get the
[2:37:32] idea of what they can use this app for.
[2:37:34] So, the templates should give them a
[2:37:36] pretty good idea. This one took a bit
[2:37:37] longer, but feature 18 is done. We now
[2:37:41] have the starter templates file. So, if
[2:37:44] you head over here and collapse
[2:37:46] everything, maybe we should start with a
[2:37:48] blank canvas, but we can keep doing it
[2:37:51] within our mess right here. Uh, at the
[2:37:53] top right there's the templates button.
[2:37:56] And if you click it, you'll see a couple
[2:37:58] of different starter templates which
[2:38:00] aren't looking that good right now. They
[2:38:03] look a bit too vertical, but yeah, as
[2:38:06] soon as you click import, it'll actually
[2:38:08] import a lot of stuff pre-labeled. Uh,
[2:38:10] but it might be better to do that within
[2:38:12] a new project so we can see it a bit
[2:38:13] better. So, I'll call it CICD
[2:38:16] and create a new project. And then we'll
[2:38:19] start from a template by going with
[2:38:22] maybe the CI/CD pipeline or let's go
[2:38:25] with microservices.
[2:38:27] And you can take a look that that
[2:38:29] immediately tells you a bit about how we
[2:38:31] can start structuring the application
[2:38:33] infrastructure. But yeah, this right now
[2:38:35] is looking a bit too vertical. The
[2:38:38] design is not actually being displayed.
[2:38:40] So we want to take this screenshot and
[2:38:42] we want to feed it into the chat by
[2:38:44] holding the shift key and then drag and
[2:38:46] dropping. And then we want to compare
[2:38:47] that with how it looks like on the
[2:38:49] finished product where we can clearly
[2:38:52] see the full template before we drag and
[2:38:54] drop it. So I'll also put that here. And
[2:38:58] I'll say I'll pass in the screenshot of
[2:39:01] how the templates look right now. They
[2:39:04] look a bit too vertical and the actual
[2:39:07] elements are not clearly visible.
[2:39:09] Whereas on another screenshot which is
[2:39:11] the finished product, you can see how
[2:39:13] each card gets its own space and they
[2:39:16] show the entire diagram or the entire
[2:39:18] template that's going to be entered in
[2:39:20] once clicked. Make it look more similar
[2:39:22] to that. So once again, this is a little
[2:39:24] corrective prompt with two different
[2:39:26] screenshots, one before and one after.
[2:39:29] Let's see how well it does. So currently
[2:39:31] it looks like this. So I'm going to snap
[2:39:34] my fingers and we come down to something
[2:39:36] that looks like this. Definitely not
[2:39:39] good. Even though now it's a bit better
[2:39:41] as it's showing the full template that's
[2:39:44] going to be inserted in, but I'm not
[2:39:46] quite sure why it cannot get the widths
[2:39:49] right. So, we could be a bit more
[2:39:50] specific and tell it to increase the
[2:39:52] width of the whole import template card
[2:39:54] and then to increase the width of the
[2:39:56] cards within it so that they're the same
[2:39:58] as this. And that's what I'll tell it
[2:40:01] for the second time by saying increase
[2:40:04] the width of the entire import template
[2:40:07] overlay. And then increase the width of
[2:40:09] the card within it as well. So it looks
[2:40:11] the same as on the final screenshot. And
[2:40:14] I'm purposefully being not as
[2:40:16] descriptive right here as we are within
[2:40:18] our spec files because I want to show
[2:40:20] you how it can cost you a lot by not
[2:40:23] being specific from the start. A lot of
[2:40:25] back and forth messages, conversations,
[2:40:27] and corrective fixes. And very soon the
[2:40:30] fix is in and now it actually looks
[2:40:32] amazing. It increased the width and it's
[2:40:34] much clearer what it's actually going to
[2:40:36] insert in. So that means that we now
[2:40:38] also officially have the templates. So
[2:40:41] we implemented a lot of stuff across
[2:40:44] these five separate feature specs. 18
[2:40:46] files changed in total which means a lot
[2:40:48] of stuff to review. This actually
[2:40:50] deserves its own pull request. So let's
[2:40:52] go ahead and push the changes either via
[2:40:54] terminal or via the source control right
[2:40:56] here. It's going to autocraft a nice
[2:40:58] message such as improved node shape,
[2:41:00] added resizing and inline labels and
[2:41:03] adding color toolbars.
[2:41:05] Then once you commit and sync back on
[2:41:08] GitHub, you'll see that the development
[2:41:10] branch had recent pushes 7 seconds ago.
[2:41:13] So let's just open up a new pull request
[2:41:15] and let's wait to provide us with a
[2:41:18] review. I think this walkthrough will be
[2:41:20] particularly useful as we've covered
[2:41:22] many different features. So, this PR
[2:41:25] implements a comprehensive canvas
[2:41:27] editing feature set, including custom
[2:41:29] edge rendering with inline labels, node
[2:41:32] resizing with color toolbars, keyboard
[2:41:34] shortcuts for zooming and undoing and
[2:41:36] redoing, a canvas control bar, and a
[2:41:39] starter template system with a modal
[2:41:41] dialogue and SVGbased previews. We've
[2:41:44] made changes across 19 different files.
[2:41:47] And here is the sequence diagram. The
[2:41:49] user clicks the templates button. It
[2:41:52] opens the editor navbar and then we open
[2:41:54] up the templates. We display the
[2:41:56] templates with card previews. The user
[2:41:59] imports them and then once they do, we
[2:42:02] pass the pending template prop. Then we
[2:42:05] forward that pending template to the
[2:42:07] canvas editor. Live blocks clears the
[2:42:09] existing nodes or edges, adds the
[2:42:11] templates, syncs this new graph to the
[2:42:13] canvas, triggers the fit view
[2:42:15] automatically, and then once it's
[2:42:17] imported, we bring it back to the user.
[2:42:20] This is a nice diagram on the starter
[2:42:22] templates feature. This was a complex
[2:42:24] PR, so I'm assuming there's going to be
[2:42:27] a lot of different things we can fix.
[2:42:29] The first one points out to exposing an
[2:42:31] accessible name on these icon buttons
[2:42:35] because title is not a dependable
[2:42:37] accessible label. It's telling us to add
[2:42:40] the area label title for the zoom, fit,
[2:42:43] undo, redo buttons for people who are
[2:42:46] using some assisted technologies. So, if
[2:42:48] I head back over here and hover over
[2:42:50] them, it will tell me that this is an
[2:42:52] undo. But for people with screen
[2:42:54] readers, this is not going to do it. And
[2:42:56] they will have no idea what these
[2:42:58] buttons are all about. I mean, it's rare
[2:43:01] that these types of people would be
[2:43:02] using this kind of an application
[2:43:04] anyway. But it's always great to
[2:43:06] implement anything you're doing with
[2:43:08] best practices in mind. So, in this
[2:43:09] case, Code Rabbit provided me with a
[2:43:11] prompt for AI agents to use. So, we can
[2:43:14] add those area labels. After that,
[2:43:16] there's a major potential issue on
[2:43:18] avoiding double committing the edge
[2:43:20] label on enter or escape. So when
[2:43:22] pressing enter or escape, it'll call the
[2:43:25] commit edit immediately. Then the inputs
[2:43:27] on blur handler will call it again when
[2:43:29] the element loses focus. This sends two
[2:43:32] mutations through live blocks, creating
[2:43:34] duplicate undo retries for a single
[2:43:36] edit. That's interesting. So the fix is
[2:43:39] simply to call the prevent default and
[2:43:41] prevent blur instead of commit edit. So
[2:43:44] let's find that. I'll find where this
[2:43:46] commit edit is getting called. It is
[2:43:48] right here in canvas edge component.
[2:43:51] Specifically, we are looking at it on
[2:43:53] the enter key or the escape key. So
[2:43:56] right here. And instead of that, we want
[2:43:58] to apply those two lines prevent blur
[2:44:02] and prevent default. And we also want to
[2:44:06] remove the commit edit from the
[2:44:08] dependency array. After that, there's a
[2:44:10] minor issue to move ref updates into a
[2:44:13] sync effect to comply with React 19 ref
[2:44:15] values. So, basically, it's telling us
[2:44:18] to put it within a use effect. That's
[2:44:20] super simple. Let's just find where in
[2:44:21] the code this is. And after that, you
[2:44:24] can see that even it's complaining right
[2:44:26] here about the code, but we didn't take
[2:44:28] a look at it because we weren't looking
[2:44:30] at the actual code. It's always good to
[2:44:32] use the best practices. So, we just need
[2:44:34] a use effect right here below. That's
[2:44:37] going to put all of these node refs into
[2:44:40] edges and nodes like this. And
[2:44:43] everybody's happy. After that, we're
[2:44:45] missing the enter key for handling the
[2:44:46] label commit. So if it says save the
[2:44:49] label on blur, enter or escape. But on
[2:44:53] handle key down, we only add escape. So
[2:44:56] right here, we also have to add the
[2:44:58] enter key. I think we searched for this
[2:45:00] across the codebase just before. That
[2:45:02] was right here in the canvas edge, but
[2:45:05] not this instance. the instance where we
[2:45:07] just had the escape. So I'll search for
[2:45:09] escape
[2:45:11] and it's right here. We have to replace
[2:45:13] it with if key is escape or if is key is
[2:45:16] enter. And once again for you these
[2:45:19] suggestions might be completely
[2:45:20] different from mine and that's normal
[2:45:22] because agentic development is not
[2:45:24] predictable. So for me it's adding some
[2:45:26] accessibility names or guarding some
[2:45:29] colors. For you it's going to be
[2:45:30] something else. But I always love
[2:45:32] learning about everything that Code
[2:45:34] Rabbit throws at me because next time I
[2:45:36] can immediately do it better. Or in this
[2:45:38] case, we can make our feature specs more
[2:45:40] specific so that our agents don't make
[2:45:43] these mistakes in the first place. Oh,
[2:45:44] and this one is interesting. When trying
[2:45:46] to undo or redo, it's currently looking
[2:45:49] only at a lowercase letter Z. But in
[2:45:51] case somebody has caps lock turned on,
[2:45:53] we also wanted to take a look at the
[2:45:55] uppercase C. This is interesting. So,
[2:45:58] let's go ahead and push those code
[2:46:00] rabbit suggested fixes.
[2:46:02] All of them were within the canvas.
[2:46:06] And then once they're up, we can simply
[2:46:09] go ahead and merge this BR.
[2:46:12] Amazing job on adding all of these
[2:46:14] little improvements that make our canvas
[2:46:17] that much more interactive.
[2:46:21] In this chapter, we'll add the
[2:46:23] collaborators avatar. So when somebody
[2:46:25] else is moving something on the screen,
[2:46:27] you can see who is messing with you.
[2:46:29] We'll also complete the chat sidebar UI
[2:46:32] and implement a canvas autosave which
[2:46:35] will save our canvas data to our versel
[2:46:37] blob so when you create something you
[2:46:40] don't lose it. And I'll break down all
[2:46:42] of these within three separate feature
[2:46:45] spec files. Each one is independent but
[2:46:47] together they complete the collaborative
[2:46:50] experience before AI generation enters
[2:46:53] the picture. So back within our
[2:46:54] application, create a new 19 presence
[2:46:59] avatars cursors.m MD chat. The goal of
[2:47:03] this spec is to implement presence
[2:47:05] avatars and cursors because right now
[2:47:09] multiple users can edit the same canvas,
[2:47:11] but they can't see each other. And after
[2:47:15] this, every connected collaborator will
[2:47:17] appear as a live cursor directly on the
[2:47:21] canvas with their name and color. So we
[2:47:24] want to render those collaborator
[2:47:26] avatars and add those cursors to the
[2:47:28] canvas. And also on the top right, we
[2:47:31] can show a stacked group of avatars
[2:47:34] where we can see everyone in the room at
[2:47:36] one place. So you know the drill. Let's
[2:47:39] get it implemented. And the presence
[2:47:41] feature has now been implemented.
[2:47:43] There's a new component rendered inside
[2:47:45] of the canvas wrapper called the
[2:47:47] presence cursor as well as the
[2:47:49] collaborators avatars. So if you head
[2:47:51] back over to a specific project, we can
[2:47:54] stay within the CI/CD. Open up this
[2:47:56] project within a second tab. And check
[2:47:58] this out. Right here on top, you should
[2:48:00] see that Adrian is also within this
[2:48:02] canvas. But in this case, both of us are
[2:48:04] Adrian's. So you can see another
[2:48:06] person's cursor. And if I put these tabs
[2:48:09] side by side, take a look at this.
[2:48:12] Using live blocks, while one user is
[2:48:15] doing something, all the other users in
[2:48:17] the room can see exactly what they're
[2:48:20] doing. So, this is a great first step
[2:48:22] toward interactivity. But we can do
[2:48:24] more. Head over and create a new feature
[2:48:27] spec or just get it from the zip called
[2:48:30] 20 AI sidebar shell.md.
[2:48:35] The goal of this one is to create a
[2:48:37] sidebar placeholder that'll later on get
[2:48:40] replaced with a proper UI. Two tabs, the
[2:48:43] AI architect and the specs. The AI
[2:48:46] architect tab will have a scrollable
[2:48:48] chat area, starter prompt, chips,
[2:48:51] message bubbles, and a composer input,
[2:48:54] while the specs tab will have a generate
[2:48:57] button and a placeholder spec card. No
[2:49:00] backend logic yet, just the UI that
[2:49:02] everything else will connect to. So
[2:49:05] let's run it and let's see how it does.
[2:49:08] And after a couple of minutes, it is
[2:49:10] done. In this case, it touched only the
[2:49:12] AI sidebar, which is a new standalone
[2:49:14] component as well as the editor
[2:49:16] workspace client where it replaced the
[2:49:19] old aside with this new AI sidebar. So
[2:49:22] now we got a new sidebar that looks
[2:49:25] something like this. You can see it on
[2:49:27] the right side. There's the AI
[2:49:29] architect, which soon enough will allow
[2:49:31] you to design full workflows and systems
[2:49:34] within the canvas, which looks like a
[2:49:36] chat because you're speaking with an
[2:49:38] agent. And then there is a specs tab,
[2:49:41] which allows you to generate a specific
[2:49:43] specification and then later on download
[2:49:45] it. This is just the UI for now, but
[2:49:47] soon enough this will become real. You
[2:49:49] can also type multiple messages by
[2:49:52] pressing shift and then enter, which is
[2:49:54] useful for those longer prompt. Oh, and
[2:49:56] before we run the next spec, which is
[2:49:58] all about autosaving what we're
[2:50:00] currently working on, we need to set up
[2:50:02] Verscell blob storage. Verscel blob is
[2:50:05] basically an object storage service.
[2:50:08] Think of it like a cloud drive for your
[2:50:10] app. So instead of storing large files
[2:50:13] directly in your database, you upload
[2:50:15] them to the blob and store only the URL
[2:50:17] reference in Prisma. We're using it for
[2:50:20] two different things in Ghost AI. canvas
[2:50:23] snapshots as save JSON and generated
[2:50:26] specs that will be available for
[2:50:28] download later on through Markdown. It's
[2:50:31] completely free to get started with. You
[2:50:33] can just head over to versell.com. Then
[2:50:35] on the left side, click storage and
[2:50:37] create a new database. Choose blob. For
[2:50:40] store name, enter something like ghost
[2:50:42] aai and we'll set it to private because
[2:50:45] private storage means that your blob
[2:50:47] URLs require a token to access. Without
[2:50:50] this, anyone who gets a hold of your
[2:50:52] blob URL can read the file directly,
[2:50:54] which means the canvas data and
[2:50:56] generated specs would be publicly
[2:50:58] readable. But private storage keeps
[2:51:00] everything scoped to your application
[2:51:02] only.
[2:51:04] So create it and once it is created,
[2:51:07] click on it and right here you'll be
[2:51:09] able to find your ENV local where you
[2:51:11] can just copy the snippet. Then within
[2:51:13] your env.local, local. You can simply
[2:51:16] add this new env blob read write token
[2:51:20] and we are ready to execute our next
[2:51:22] feature spec by adding a file called 21
[2:51:26] canvas autosave.md.
[2:51:30] Before we add that AI generation canvas
[2:51:33] state needs to persist. So after this
[2:51:36] every change to the canvas is
[2:51:37] automatically saved to versel blob which
[2:51:40] we just set up. And then we'll save the
[2:51:42] blob URL, store it in Prisma, and our
[2:51:44] canvas data will be saved securely. So
[2:51:47] this spec is all about saving the
[2:51:49] current canvas state. It should be
[2:51:52] pretty simple for our agent to implement
[2:51:54] given that we gave it all the
[2:51:55] information about the versel blob and
[2:51:57] about the environment variable that it
[2:51:59] can use to save data. And after a couple
[2:52:02] of minutes, it is done. A versel blob is
[2:52:05] installed and blob readr token is
[2:52:08] already present in the env.local.
[2:52:10] But if we get back to the editor, at
[2:52:12] least on my end, there seems to be a
[2:52:14] bug. So, let me show you how I would
[2:52:16] approach fixing it. To fix this issue,
[2:52:19] you can just copy it, head back over to
[2:52:21] our application, specifically into the
[2:52:25] current issues.mmd, and specify that
[2:52:28] this is the current
[2:52:31] error that I'm seeing on the screen. And
[2:52:35] you can paste it right here. It's going
[2:52:36] to give it all the necessary information
[2:52:38] and you can say fix it.
[2:52:42] So make sure that it has access to the
[2:52:44] current issues and say fix it or you
[2:52:47] could have just pasted that into the
[2:52:48] chat itself. For just a singular issue
[2:52:51] like this, it should be totally okay.
[2:52:53] And as it's working through it, I can
[2:52:55] already see what was the issue. Even
[2:52:57] though we ran MPX Prisma generate and
[2:52:59] migrate, the generated client is
[2:53:02] correct, but there's a stale. Next cache
[2:53:05] bundling the old schema. So, it's going
[2:53:07] to clear the old cache and then delete
[2:53:10] it, which forces TurboAC to recompile
[2:53:12] from a freshly generated Prisma client,
[2:53:14] which already has the canvas blob URL.
[2:53:17] Then, we just have to restart our server
[2:53:19] and the error will be gone. So open up
[2:53:21] your terminal and just rerun it by
[2:53:23] saying mpm rundev and then back on
[2:53:25] localhost 3000. If you reload the error
[2:53:28] will be gone. So now we are ready to
[2:53:30] test that final feature we implemented.
[2:53:33] Head over to one of the active projects.
[2:53:35] Add a couple of nodes right here.
[2:53:37] Refresh the page and make sure it
[2:53:39] remains at the exact space where you
[2:53:40] left it at. So, I'll try to change its
[2:53:43] name and move it below the O service and
[2:53:46] just make sure that it actually remains
[2:53:47] there, which would mean that the
[2:53:48] autosave is working. Perfect. But even
[2:53:52] though it saved it, it wasn't saved
[2:53:54] through a blob because if you head over
[2:53:55] to the Ghost AI blob storage, you'll see
[2:53:58] that there is absolutely nothing there.
[2:54:00] So, let's fix this issue and a couple
[2:54:03] others. I went through the application,
[2:54:06] tested it deeply, and came up with a
[2:54:08] couple of different issues that I added
[2:54:10] in the current issues.md file. You
[2:54:13] should already have a file like this in
[2:54:15] your zip, which you can just refer to.
[2:54:17] But again, it's possible that for you,
[2:54:19] you'll have to go through the app
[2:54:20] yourself, try to find some specific
[2:54:22] issues within your app, and then write
[2:54:24] the prompt to fix them. But yeah, in
[2:54:27] this case, let's go over the most
[2:54:29] important one, which is the saving
[2:54:31] button in the workspace navbar. Uh the
[2:54:33] workspace snapper is missing a save
[2:54:35] button. The autosave hook exists but we
[2:54:38] need to wire the button to it. It should
[2:54:41] default to save. While saving it should
[2:54:44] switch over to saving. After successful
[2:54:46] save it should switch over to save. And
[2:54:48] that's it. The most important thing that
[2:54:50] I noticed right here is in this canvas
[2:54:54] route. TS file if you take a look at the
[2:54:57] blob storage the access is set to
[2:55:00] public. And remember what I said before,
[2:55:02] it has to be set to private because we
[2:55:05] don't want other people to be able to
[2:55:07] view the changes we make within the
[2:55:08] canvas. So we need to set it to private
[2:55:11] and we're not asking it to change
[2:55:12] anything else for now. For now, I just
[2:55:14] want to focus on issue one and then
[2:55:16] later on go through all of the other
[2:55:18] issues. So yeah, let's ask it to fix the
[2:55:21] save button first. I'll open up a new
[2:55:23] chat and tell it to read the current
[2:55:26] issue MD file. Check the issue one and
[2:55:28] fix it. After fixing it, mark it as
[2:55:31] pending to test. Let's run it and see
[2:55:33] how well it does. And very quickly,
[2:55:36] issue one is fully implemented and
[2:55:38] marked as pending for tests. So, let's
[2:55:41] go ahead and test it out. You can see
[2:55:42] the save button right here. And as you
[2:55:44] move something on the screen and change
[2:55:46] its color and click save, you can see
[2:55:49] that the saving indicator is not really
[2:55:51] changing. So, you can quickly head over
[2:55:53] to the codebase. See, there's no errors
[2:55:55] in the terminal, but it's still not
[2:55:57] doing its thing. So let's send it one
[2:55:59] quick corrective prompt by telling it
[2:56:01] that issue one still hasn't been fully
[2:56:04] fixed. The saving status indicator is
[2:56:07] not being changed and when I click the
[2:56:09] save button nothing is changing either
[2:56:11] analyze the issue further and fix it and
[2:56:14] we can send it out and it was doing a
[2:56:16] bit of thinking but it came back with a
[2:56:18] response that the root cause was react
[2:56:22] mode enabled by default in nextJS app
[2:56:24] router. It double invokes effects in
[2:56:27] development. So on initial mount, the
[2:56:29] cleanup is intentionally fired by the
[2:56:31] strict mode before remount and then
[2:56:34] remount effect only registers the
[2:56:36] cleanup again, but it never resets. So
[2:56:38] that means that the ismounted is
[2:56:40] permanently set to false in development.
[2:56:42] So the save exited every time. This fix
[2:56:45] removes the ismounted refer
[2:56:48] uh because React 18 made this guard
[2:56:50] unnecessary. Perfect. So, if we head
[2:56:52] back right here and reload, and if you
[2:56:54] move something around and then press
[2:56:57] save at the top right,
[2:57:00] you can see that it says saving. And
[2:57:02] then we get an error. Save failed. If I
[2:57:05] move it again a couple of times and
[2:57:07] click save again, it says save failed.
[2:57:11] It's funny because when I tested it
[2:57:13] initially, it actually said saving and
[2:57:15] then saved. So back in the blob storage,
[2:57:18] you can see that I have this new canvas
[2:57:20] and it actually stored the JSON data.
[2:57:22] But then when I try doing it again, it
[2:57:25] failed. So if you open up the terminal,
[2:57:27] you'll see that we have an error with
[2:57:29] the versel blob saying that the blob
[2:57:32] already exists. So we should add allow
[2:57:34] override is set to true if we want to
[2:57:37] override it. So what we can do is simply
[2:57:40] find this file that's the canvas root.
[2:57:42] So you can go over to canvas root and
[2:57:46] just add an additional prop of allow
[2:57:49] overwrite is set to true. This single
[2:57:52] line should immediately allow us to save
[2:57:55] every other time
[2:57:58] not just the first time. You can see it
[2:58:00] says saved and back when the blob you
[2:58:02] can see that it got modified less than a
[2:58:05] minute ago which means that it is
[2:58:07] consistently saving data. And right now
[2:58:09] the size of this JSON file is 6.11
[2:58:12] kilobytes. But if we head back and add a
[2:58:14] couple more labels and models and shapes
[2:58:18] and some pieces of text within them and
[2:58:20] then save again and then head to the
[2:58:22] blob, you can see that now the size
[2:58:24] increased which means that it is
[2:58:26] properly saving all the data. So now
[2:58:29] that our issue one has been fixed right
[2:58:31] here, uh we can ask it to continue
[2:58:33] fixing the other issues. uh specifically
[2:58:36] some issues that are found are about
[2:58:39] deleting nodes and edges. Uh so right
[2:58:42] now we don't have a way to delete
[2:58:44] anything. So if I try pressing backspace
[2:58:47] or the delete keys or anything, I can't
[2:58:50] do it. So the solution is simple. We
[2:58:52] just need to add a key down event
[2:58:54] listener to the canvas that listens for
[2:58:57] the delete and backspace keys. doesn't
[2:58:59] fire when the event target is an input
[2:59:01] or text area but just gets fired when we
[2:59:04] are selecting specific nodes and then it
[2:59:07] deletes them. As the third issue uh
[2:59:10] currently we can also just connect from
[2:59:12] top to the top of the handle. You can
[2:59:16] see even if I drag from the right handle
[2:59:18] it connects from top to top. We want to
[2:59:21] be able to drag and drop from any side
[2:59:24] of the element to any other side. that
[2:59:27] will allow us to make these graphics so
[2:59:29] much more customizable. So, we just want
[2:59:32] to allow it to be connected from top,
[2:59:34] right, bottom, and left. Then, as the
[2:59:37] fourth issue, I noticed that when I drag
[2:59:39] and drop specific elements, they drop a
[2:59:42] bit lower than where they're supposed
[2:59:44] to. So, I just wanted to fix that
[2:59:46] offset.
[2:59:48] And notice when I dragged and dropped
[2:59:50] it, it actually said saving at the
[2:59:52] bottom left right here. And then saved,
[2:59:54] which means that the autosave
[2:59:55] functionality is working. And then the
[2:59:58] fifth issue is the auto zoom on first
[3:00:01] node. We want to read the live blocks
[3:00:03] agent skills before implementing it. And
[3:00:05] then as soon as we drop it, we want to
[3:00:07] zoom it in. And for six and seven, we
[3:00:09] want to check the clerk skills. Um, and
[3:00:11] we have some issues with the
[3:00:13] collaborator avatar images. If the image
[3:00:15] is coming from clerk, we want to add it
[3:00:17] to next config so it gets properly
[3:00:19] shown. And also currently we have two
[3:00:23] different clerk buttons. We just want to
[3:00:25] keep the one and remove the other one.
[3:00:27] So let's ask it to fix the errors from
[3:00:30] two all the way to 7. Okay. Now that the
[3:00:34] issue one in the current issues.md file
[3:00:36] has been fixed, uh analyze and fix
[3:00:39] issues from 2 to 7. Press enter and
[3:00:43] let's see how well it does. Okay, it
[3:00:46] looks like all the remaining issues have
[3:00:48] been implemented and uh it marked them
[3:00:51] for pending test. Uh which is a good
[3:00:53] thing for us to test. Right now we have
[3:00:55] to test deleting the nodes and edges um
[3:00:59] handling uh the positions or the lines
[3:01:02] in between the elements, draw position
[3:01:04] offset, auto zooming and then clerk
[3:01:07] images. So, if I head back right here
[3:01:10] and reload the page, let's first test
[3:01:12] the drag and drop. So, if I try to drag
[3:01:14] and drop it here, you can see that it
[3:01:17] gets placed at the exact position. This
[3:01:19] is pretty crazy. Take a look at once
[3:01:21] again. I'll try to place it right here.
[3:01:24] And it worked. Of course, it's going to
[3:01:26] depend on the zoom position. I think if
[3:01:28] we at a normal regular zoom and you once
[3:01:31] again drag and drop it to a specific
[3:01:32] position, that's exactly where it places
[3:01:34] it. So, that has been fixed. Also, now
[3:01:38] there's just one clerk icon right here
[3:01:40] where you can see your account. Uh, what
[3:01:42] else did we fix? The edges connections.
[3:01:46] So, for example, let's try to drag and
[3:01:48] drop the bottom of this edge right here
[3:01:50] to the left side of the test suite. And
[3:01:53] take a look at how well it connects. It
[3:01:56] even places the arrow from here to here.
[3:01:58] Or maybe when I go into the package,
[3:02:00] that works as well. And the arrows move.
[3:02:03] This makes our application so much more
[3:02:05] usable because now for example we can
[3:02:07] connect the O service horizontally with
[3:02:10] the database and then take the database
[3:02:13] output and do something with it. Again
[3:02:17] this canvas is becoming a mess right now
[3:02:19] because there's so much stuff happening.
[3:02:21] So it would make sense to test out
[3:02:23] delete. Select a couple of elements and
[3:02:25] try to press the backspace or the delete
[3:02:28] key and see whether it's going to remove
[3:02:31] them. because for me it doesn't. So it
[3:02:34] looks like that's the last issue that's
[3:02:36] still pending. So let's just tell it
[3:02:38] that issue two remains unfixed. When I
[3:02:42] select an element and press the
[3:02:43] backspace or the delete key, the element
[3:02:46] is still there and isn't being deleted
[3:02:48] from the canvas. Analyze it and fix it.
[3:02:51] So let's see if we can just narrow it
[3:02:53] down to one issue whether it can finish
[3:02:55] that last one. And again, this just
[3:02:58] shows you that whenever you give it more
[3:02:59] stuff to fix, uh it's easy for some of
[3:03:02] these to uh fall through because it
[3:03:05] maybe didn't analyze them as deeply in
[3:03:08] isolation. Uh so you can see why these
[3:03:11] feature specs worked so well so far
[3:03:14] because they were super detailed and
[3:03:16] well documented. But as soon as you go
[3:03:18] deeper into the conversation, the agent
[3:03:20] can easily get lost.
[3:03:22] So this is its last chance. Let's see
[3:03:24] how well it does.
[3:03:27] It looks like it was able to find a root
[3:03:29] cause in about 30 seconds. In apply node
[3:03:32] changes inside of the liblocks react
[3:03:35] flow source. We had a case of remove
[3:03:38] which was not doing anything. Uh so it
[3:03:41] was silently ignoring the remove type
[3:03:43] changes. Whereas livelocks exposes a
[3:03:47] dedicated ondee function that correctly
[3:03:50] deletes from the live map. So it fixed
[3:03:53] it and let's see how well it does right
[3:03:55] now. I'll reload the page and then I'll
[3:03:58] select a couple of elements and press
[3:04:00] the backspace key and now it deletes
[3:04:02] them properly. Now, if you don't want to
[3:04:04] delete them one by one, you can also
[3:04:06] hold the shift key and then drag and
[3:04:09] drop over multiple and remove them that
[3:04:11] way. Also, another thing that I didn't
[3:04:13] tell you so far is that you can also add
[3:04:16] uh text to the lines connecting
[3:04:19] different elements like we want to build
[3:04:22] and then run the test suite. So, this
[3:04:27] way kind of it makes more sense with the
[3:04:29] connection, but you can also use the
[3:04:31] text on the lines for significantly more
[3:04:34] detailed instructions when it comes to
[3:04:36] connecting different elements. But yeah,
[3:04:38] now that all of these issues are fixed,
[3:04:40] we can go ahead and push them. So say
[3:04:42] get add dot get commit-m and this lesson
[3:04:46] was all about canvas interaction. So say
[3:04:48] implement improved canvas interaction
[3:04:53] and then run get push. Now in the next
[3:04:55] lesson we'll focus on the AI
[3:04:58] collaborative side of the application.
[3:05:02] And now that we have the full canvas
[3:05:05] right here where we can drag and drop
[3:05:08] elements, move things around and create
[3:05:10] our own architectural systems, we are
[3:05:13] ready to help our users a bit by
[3:05:16] implementing the AI workspace where we
[3:05:20] can allow our users to collaborate with
[3:05:22] our AI agent within the application that
[3:05:25] I'll teach you how to implement right
[3:05:27] now. But I want you to think about it a
[3:05:29] bit like before we start building the AI
[3:05:32] generation features um you need to
[3:05:35] understand why these can't run inside a
[3:05:38] normal API route. See, when a user sends
[3:05:41] a prompt to Ghost AI, something like
[3:05:44] this, to design an e-commerce backend,
[3:05:47] the agent doesn't just make one call. It
[3:05:49] analyzes the request, runs multiple AI
[3:05:52] steps, generates nodes and edges, and
[3:05:56] syncs everything back to the canvas, all
[3:05:58] while keeping the user updated. And that
[3:06:00] can easily take 30 to 60 seconds, maybe
[3:06:03] even a couple of minutes. And I mean
[3:06:05] you've already seen this pattern when
[3:06:07] you generate an image with Chad GPT or
[3:06:09] Gemini. It doesn't happen instantly. The
[3:06:12] work runs in the background and you keep
[3:06:15] receiving the updates until the response
[3:06:16] is ready. And the API routes within our
[3:06:19] application are not designed for that.
[3:06:21] They have execution limits which means
[3:06:23] that long running requests can time out.
[3:06:26] And even if they didn't, keeping a
[3:06:28] request open for that long isn't how
[3:06:30] production systems are built. That's
[3:06:31] when I'll teach you how to implement
[3:06:33] trigger dev to solve this problem. In
[3:06:36] the final version of the application, if
[3:06:38] you give it a detailed prompt and send
[3:06:40] it, you'll be able to see direct updates
[3:06:44] as it is working on the thing. It'll
[3:06:47] first start with analyzing your
[3:06:48] architecture request and all of these
[3:06:51] functions will run as durable background
[3:06:54] tasks outside of the request life cycle
[3:06:57] which means that the work is running in
[3:07:00] the background and you'll be updated on
[3:07:02] the process. So the work of the API
[3:07:04] route is to just trigger the task and
[3:07:06] then return while the heavy work
[3:07:08] continues in the background. And that's
[3:07:10] why both the AI design generation and
[3:07:13] the spec generation in Ghost AI run
[3:07:16] through trigger dev instead of directly
[3:07:18] in API routes. And even before we used
[3:07:21] trigger on Ghost AI, I was already using
[3:07:24] it within jsmastery.com platform where
[3:07:27] every time that users go through
[3:07:29] different lessons, check out the
[3:07:30] overviews, contents or transcripts, we
[3:07:32] can perform some actions on the back end
[3:07:35] without slowing down or freezing what
[3:07:37] the user can see on the front end, which
[3:07:39] is super helpful for quizzes or sharing
[3:07:42] the status of the AI interviewer that we
[3:07:44] worked on. So yeah, let me show you how
[3:07:46] we can set up trigger dev in your
[3:07:48] project.
[3:07:49] First, click the link down in the
[3:07:51] description to be able to follow along
[3:07:53] and see exactly what I'm seeing and then
[3:07:56] create a new account. Once you're in,
[3:07:58] you should be able to see your dashboard
[3:08:00] that looks something like this. So, go
[3:08:02] ahead and create a new project. I'll
[3:08:05] call it Ghost AI.
[3:08:08] We are working on an AI agent. And under
[3:08:11] technologies, I thought that Gemini
[3:08:13] works the best. So, you can proceed with
[3:08:15] Google Gemini. And what are we trying to
[3:08:17] do with trigger? Well, we're still
[3:08:19] learning how trigger works as well as
[3:08:21] potentially shipping a production
[3:08:23] workflow. So, let's create it. Then,
[3:08:25] once it is created, you can run this CLI
[3:08:29] command to initialize it in the existing
[3:08:31] project. So, just copy it, head back,
[3:08:35] open up the terminal. You can do it
[3:08:37] under a new tab, and just run MPX
[3:08:41] trigger.dev at latest init. and then
[3:08:44] pass your specific project ID. Say yes
[3:08:47] to install the TriggerDev CLI. And this
[3:08:50] will now install the Trigger Dev SDK and
[3:08:53] initialize the config file. But it'll
[3:08:55] first ask you a couple of questions such
[3:08:58] as choose how you want to initialize
[3:09:00] your project. In this case, we'll
[3:09:02] proceed with the Trigger Dev MCP, which
[3:09:05] allows you to vibe your way to a new
[3:09:07] project. Well, in this case, write
[3:09:09] detailed project specifications to come
[3:09:12] up with a new scalable project. It's
[3:09:14] going to ask you whether you want to
[3:09:15] restrict the MCP server to the dev
[3:09:17] environment only. I'll say no. And then
[3:09:20] you'll be able to choose one or more
[3:09:22] clients to install the MCP server into.
[3:09:25] You can choose all the ones that you're
[3:09:26] using such as Cloud Code, VS Code,
[3:09:30] OpenAI Codeex, or really anything else
[3:09:32] that you want. And then press enter.
[3:09:35] Where should the MCP server for cloud
[3:09:37] code be installed? I'll go over with the
[3:09:40] project.
[3:09:42] Same thing for all the other ones.
[3:09:45] And that's it. We now need to restart
[3:09:47] our MCP clients. In your client, look
[3:09:50] for a server named trigger and then get
[3:09:52] started with Trigger Dev by asking it to
[3:09:55] add Trigger to our project. So, let's do
[3:09:58] just that. I'll open up our Claude code
[3:10:01] and that's going to be on a new chat
[3:10:03] window. And I'll simply tell it to add
[3:10:05] trigger dev to my project. And we can
[3:10:07] now run it. But just before I do, I want
[3:10:10] to share another thing with you. And
[3:10:12] that is that trigger also supports agent
[3:10:15] skills to teach any AI coding assistant
[3:10:17] best practices for writing tasks,
[3:10:20] agents, and workflows. So we can install
[3:10:22] it as we did for all the other dev tools
[3:10:25] by opening up the terminal and running
[3:10:28] mpx skills at trigger.dev skills.
[3:10:32] We can choose uh trigger agents, config,
[3:10:36] and maybe setup. I think that's going to
[3:10:38] be all we need for now, but you can just
[3:10:40] go ahead and add all of them as well.
[3:10:43] Choose your specific agents you want to
[3:10:45] add it for. Do it within the projects
[3:10:48] through Sim Link and then quickly
[3:10:51] install it. Now, let's go ahead and ask
[3:10:54] it to add Trigger Dev to my project.
[3:10:56] Then, let's run it. It's going to
[3:10:58] explore the project structure, find all
[3:11:00] the relevant files and the architecture
[3:11:02] context, which matters a lot. It's going
[3:11:04] to get the full picture, and it'll start
[3:11:07] with configuring the trigger config.ts,
[3:11:10] creating a trigger directory with
[3:11:12] example tasks, adding the trigger.dev
[3:11:15] route handler, and finally updating the
[3:11:17] progress tracker. And there we go. After
[3:11:19] a couple of minutes, the trigger dev is
[3:11:21] now set up. So, it first added the
[3:11:24] trigger config.js. js. So let's quickly
[3:11:28] go over into it. That's going to be
[3:11:31] within our trigger.config.ts
[3:11:34] in the root of the application and it
[3:11:37] looks something like this. It is coming
[3:11:39] from trigger dev SDK. We define a
[3:11:42] specific configuration and then we need
[3:11:45] to connect it to a project reference.
[3:11:48] This is coming from our environment
[3:11:50] variables. So very soon we'll have to
[3:11:52] find it in our trigger dev dashboard and
[3:11:53] then add it to ourvves. Then below the
[3:11:57] project we can add a runtime and set the
[3:12:00] environment to node. When it comes to
[3:12:03] directories /trigger is going to be fine
[3:12:06] or in this case I think we can just
[3:12:07] leave it to trigger. Now max duration
[3:12:10] stands for the max compute seconds a
[3:12:13] task is allowed to run.
[3:12:15] If the tasks exceed this duration, it'll
[3:12:18] be stopped. And by default, we can set
[3:12:20] it to something like 3600
[3:12:23] so that any task can run up to an hour
[3:12:25] before it stopped. But again, that's not
[3:12:28] needed because most of our AI tasks will
[3:12:30] be done in a couple of minutes. And then
[3:12:32] for the retries, if something fails,
[3:12:35] Trigger Dev will retry it up to three
[3:12:37] times with increasing delays between
[3:12:40] each attempt. So having that built right
[3:12:42] in to make sure that if something does
[3:12:43] go wrong, which it often does with AI
[3:12:45] generation, it retries it. So when your
[3:12:48] user comes back to your app, whatever
[3:12:50] they were waiting for from an AI agent
[3:12:52] is waiting for them there. Okay. So
[3:12:54] let's get those keys. I'll head back
[3:12:56] over to Trigger Dev. Specifically,
[3:12:58] scroll down to API keys. And right here,
[3:13:01] you'll be able to find your secret key.
[3:13:04] So simply copy it. Then head over into
[3:13:07] your env.local.
[3:13:10] And here we can add as it specifies the
[3:13:14] trigger project ref as well as the
[3:13:17] trigger secret key. So the secret key is
[3:13:20] the one we just copied. And the project
[3:13:21] key you can find right here by going
[3:13:23] over to the tasks and copying it right
[3:13:26] here from the end part of the CLI init
[3:13:30] command. And then just paste it over
[3:13:33] here. And the next part is to start your
[3:13:36] local dev workflow. And I think this is
[3:13:38] the exact second step from our 3minut
[3:13:41] setup. MPX trigger dev at latestdev. So
[3:13:45] you can open up your terminal. Make sure
[3:13:47] that it's not the one running your
[3:13:48] application. And before we run this, let
[3:13:51] me actually explain what it does. This
[3:13:53] is specific to local development.
[3:13:55] Trigger dev background tasks don't run
[3:13:58] on your machine automatically. They need
[3:14:00] a local worker process running alongside
[3:14:03] your next.js dev server. So just run
[3:14:06] this command. Would you like to install
[3:14:08] the trigger dev code agent rules? Well,
[3:14:10] yeah. Go ahead. We can select it for
[3:14:13] cloud code or whichever other agent
[3:14:15] you're using and choose the rules you
[3:14:17] want to install. Uh let's go with basic
[3:14:19] advanced. You know what? Let me go with
[3:14:22] all of them.
[3:14:24] Now it's going to wait for you to log in
[3:14:26] to your Trigger Dev account, which you
[3:14:28] can do by simply heading over to this
[3:14:30] URL and then authenticating your
[3:14:32] account. Once you're successfully
[3:14:34] authenticated, you can head back and
[3:14:36] you'll be able to see a screen that
[3:14:38] looks something like this.
[3:14:40] Log in successfully. Trigger dev is
[3:14:42] running and the local worker is ready.
[3:14:46] So keep this running whenever you're
[3:14:47] developing locally because without it,
[3:14:49] any task you trigger will cue but never
[3:14:52] execute. And in production on Versell,
[3:14:55] this isn't needed because trigger dev
[3:14:57] will handle the worker infrastructure
[3:14:59] for you. So, if you now head back over
[3:15:01] to your dashboard, you'll be able to see
[3:15:03] two different tasks, generate design and
[3:15:06] generate spec, which is absolutely
[3:15:08] amazing. This was going to be one of my
[3:15:10] upcoming project specifications to add,
[3:15:12] but it looks like the MCP already
[3:15:15] figured out exactly what we want and it
[3:15:17] created those tasks right here. So, soon
[3:15:19] enough, you'll be able to see how those
[3:15:21] tasks actually run and then see more
[3:15:24] information about it. So that was it for
[3:15:26] the setup and then in the next lesson,
[3:15:28] let's build the AI generation logic.
[3:15:33] Okay, Trigger Dev and the agent together
[3:15:36] already created for us the task
[3:15:38] skeletons, but in this lesson, we'll
[3:15:41] build the full AI generation flow. Now,
[3:15:44] before we make our systems design agent
[3:15:46] logic, we'll have to install a couple
[3:15:49] more packages. So, open up your
[3:15:51] terminal. We'll have to go with the
[3:15:52] third one right here. and run mpm
[3:15:56] install at trigger.dev/react
[3:15:59] hooks which lets the front end subscribe
[3:16:02] to a live trigger dev background run
[3:16:04] without manually pulling. So think of it
[3:16:07] like instead of asking is the job done
[3:16:09] yet every few seconds. The hook will
[3:16:12] stream in real time status updates
[3:16:14] directly to the UI as the task
[3:16:17] progresses. Then there's the at AI SDK
[3:16:20] Google which is the Google provider for
[3:16:22] the Verscell AI SDK. And in this case,
[3:16:25] we'll be using Gemini for both design
[3:16:27] generation and spec generation. But of
[3:16:29] course, feel free to use any other agent
[3:16:31] you prefer. And finally, AI is the core
[3:16:34] Versel AI SDK, which is going to give us
[3:16:37] utilities for generating text or
[3:16:39] generating different objects by working
[3:16:41] consistently with any kind of AI
[3:16:43] provider. So, go ahead and install these
[3:16:46] three. And while they're getting
[3:16:47] installed, head over to
[3:16:49] aistudio.google.com,
[3:16:51] which we're going to connect with
[3:16:53] TriggerDev to infuse it with all sorts
[3:16:55] of different functionalities. So, click
[3:16:57] get started. Make sure to authenticate
[3:16:59] with your account.
[3:17:01] And Google AI Studio will give you free
[3:17:04] credits in most regions, which is going
[3:17:06] to be enough to test out the generation
[3:17:07] flow throughout this build. So, click
[3:17:10] get API key. Then, create a new API key.
[3:17:14] You can call it something like ghost AI
[3:17:18] and then you'll be given all your API
[3:17:20] key details. So first copy the actual
[3:17:22] API key and paste it into yourv.local.
[3:17:28] Specifically that's going to be under
[3:17:31] google_ai_appi_key
[3:17:35] and it's going to be set to this key you
[3:17:38] just copied. Or if you want to get a
[3:17:40] completely free alternative to Google
[3:17:43] Gemini, Open Router has a pretty good
[3:17:45] selection of free models, I'd recommend
[3:17:48] this Nvidia Numatron 3 Nano Omni. That's
[3:17:51] a mouthful, which is a free model that
[3:17:54] has a 256,000 context window and it
[3:17:58] handles the architecture generation
[3:18:00] pretty well. Just keep in mind that the
[3:18:01] free tier models always have usage
[3:18:03] limits. So if you go that route, simply
[3:18:06] swap that AI SDK Google thing for the
[3:18:09] open router SDK in the generation task.
[3:18:12] For this video, I'll personally use
[3:18:13] Google AI Studio, but again, as with the
[3:18:16] AI agents, follow along with whichever
[3:18:18] one works for you. So now with the setup
[3:18:21] ready, we are ready to start adding the
[3:18:23] trigger dev task spec files. So head
[3:18:27] over into our context feature specs and
[3:18:30] find or create a new one called 22
[3:18:34] design agent API.md.
[3:18:38] The goal of this feature is to set up
[3:18:40] the backend flow for design generation
[3:18:43] using trigger dev. And keep in mind that
[3:18:45] when we're referring to design here,
[3:18:47] we're referring to the systems or
[3:18:49] architecture design of our applications.
[3:18:51] So, we're setting up this design agent
[3:18:53] API for the backend wiring. Starting
[3:18:56] with the trigger route where we need to
[3:18:59] create a specific post route that should
[3:19:01] accept the design prompt and some
[3:19:03] context and then trigger the design task
[3:19:06] through trigger dev because as I said
[3:19:09] these tasks and these AI prompts can
[3:19:11] take some time to process. Then we'll
[3:19:13] add task tracking. This is going to be a
[3:19:16] special model in Prisma to track
[3:19:18] triggerdev runs and verify ownership.
[3:19:21] Who created the run, when, and what is
[3:19:24] it all about. We should add the token
[3:19:26] route to verify ownership and then
[3:19:29] finally create the actual design task.
[3:19:32] We want to check the existing trigger
[3:19:34] dev setup and installed agent features.
[3:19:36] Reuse the existing setup, export a
[3:19:39] minimal design task, and for now, not
[3:19:41] add any design logic yet. just the
[3:19:44] infrastructure that makes the next spec
[3:19:46] possible. You learned that already. Spec
[3:19:49] by spec, we're getting closer to the
[3:19:51] final solution.
[3:19:53] So, let's go ahead and run it. As usual,
[3:19:56] you can just tell it to read the current
[3:19:58] file, update the context progress
[3:20:01] tracker, and implement it exactly as
[3:20:03] specified. And after some work, feature
[3:20:06] 22, the design agent API has now been
[3:20:09] completed. It created a new Prisma model
[3:20:13] called task run with run ID, project ID,
[3:20:16] user ID, so we know which projects are
[3:20:18] being run over in trigger dev. Then
[3:20:20] there's the design agent itself, which
[3:20:23] is a minimal task accepting a prompt in
[3:20:26] a room ID, which logs and echoes the
[3:20:28] inputs. So if you open it up, you'll see
[3:20:31] that it looks like this. Currently,
[3:20:33] there's no logic and functionality, but
[3:20:36] we'll add it very soon. Then there's the
[3:20:39] post API AI design which requires
[3:20:42] authentication and what this one does is
[3:20:44] it basically figures out whether the
[3:20:46] user is authenticated, takes in the body
[3:20:49] and finally creates a new task run in
[3:20:51] the database. But of course before it
[3:20:54] hands it over to trigger dev. But now
[3:20:57] the actual task is pretty empty. It's
[3:20:59] just console logging design agent
[3:21:01] triggered and it's not doing anything
[3:21:03] else. So our next task is to implement
[3:21:07] the full AI design agent logic so a user
[3:21:10] prompt results in real-time updates on
[3:21:13] the canvas. To do that, head over into
[3:21:15] our feature specs. And let's focus on
[3:21:18] adding the 23rd spec, which is design
[3:21:21] agent
[3:21:23] logic.md.
[3:21:25] And as I said, the goal here is to
[3:21:27] implement the full AI design agent
[3:21:30] logic. So first we need to update the
[3:21:32] file which was just created before we
[3:21:35] want to check the product behavior of
[3:21:36] the system. Check the live blocks and
[3:21:38] trigger agent skills. This is very
[3:21:40] important. Sometimes you have to
[3:21:42] explicitly tell it to check the skills.
[3:21:44] Follow the trigger dev setup and agent
[3:21:46] patterns already set up. Reuse the
[3:21:48] existing lib blocks flow and presence
[3:21:50] patterns instead of creating new ones.
[3:21:52] And then implement use Gemini logic to
[3:21:56] interpret the user prompt. Update the
[3:21:59] canvas using the collaborative flow
[3:22:01] utilities supporting actions like adding
[3:22:04] nodes, moving them, resizing them,
[3:22:06] updating them, deleting them. Basically,
[3:22:08] everything that our application is
[3:22:10] already doing. Then we want to publish
[3:22:12] that AI activity to the shared status
[3:22:14] feed so all users can see the progress,
[3:22:17] update the AI presence through cursors
[3:22:19] and thinking state and push clear status
[3:22:22] messages at key steps. If you think
[3:22:25] about it, this is a very important and
[3:22:28] big feature spec, maybe the biggest one
[3:22:31] in our application so far because now we
[3:22:33] are essentially telling our AI agent and
[3:22:36] trigger to figure out the entirety of
[3:22:40] our application and to replicate its
[3:22:43] functionality on its own while following
[3:22:46] the user prompt like the user is telling
[3:22:49] it to create something on the canvas and
[3:22:51] it should create it. So, let's go ahead
[3:22:54] and see how well it does by opening up a
[3:22:56] new clot code window, giving it access
[3:22:59] to the file, and asking it to read the
[3:23:02] spec file,
[3:23:04] update the progress document, and
[3:23:07] implement it exactly as specified. This
[3:23:10] is a big one, so I'm super excited to
[3:23:12] see how well it actually does it. And
[3:23:14] feature 23 is now complete. Uh, this one
[3:23:17] took a bit longer because it's a it's a
[3:23:19] huge one. And we now have a full AI
[3:23:23] agent built within our application
[3:23:25] powered by trigger.dev.
[3:23:27] It uses Gemini 2.0 Flash via create
[3:23:31] Google generative AI plus generate text
[3:23:34] with output object to produce a typed
[3:23:37] list of canvas actions for adding,
[3:23:40] moving, resizing, updating, and deleting
[3:23:43] nodes and edges. It sets the AI presence
[3:23:46] by thinking is set to true. So all
[3:23:48] collaborators can see the AI cursor. It
[3:23:51] broadcasts three different statuses,
[3:23:53] start, thinking, and complete. And it
[3:23:56] applies all mutations atomically in a
[3:23:59] single mutate storage call. Perfect.
[3:24:02] This is exactly what we wanted. So while
[3:24:04] we can't see it on the screen just yet,
[3:24:07] what we can do is head over to our
[3:24:10] trigger.dev dashboard under tasks.
[3:24:13] Currently, we have three separate tasks.
[3:24:15] That's because our initial setup task
[3:24:17] created the skeletons for generate
[3:24:19] design and generate spec, but the new
[3:24:21] one is right here under design agent.
[3:24:23] So, what we can do is maybe we can clean
[3:24:26] up the other two just so they're not
[3:24:28] confusing us. So, under trigger, we can
[3:24:30] remove the generate design and generate
[3:24:32] spec, which are just empty placeholders.
[3:24:36] And instead, we can just leave the
[3:24:37] design agent right here. So, that's the
[3:24:40] only one that remains. Now open it up
[3:24:43] and perform a test run. It's going to
[3:24:46] ask you to pass the data as a regular
[3:24:48] user would through the application. And
[3:24:51] we can write something like room ID. And
[3:24:53] you'll have to get this room ID directly
[3:24:55] from one of your canvases. So head over
[3:24:58] here and create a new project. Let's
[3:25:01] call it something like um system design.
[3:25:06] Create it. And you can copy the project
[3:25:08] ID directly from the URL right here at
[3:25:11] the top.
[3:25:13] Then if you head back, you can update it
[3:25:15] over here. And we can ask it to
[3:25:17] architect a real-time chat application.
[3:25:20] I need a websocket server for live
[3:25:23] messaging, a present service to track
[3:25:25] online users, and a relational database
[3:25:27] for message history. Connect the
[3:25:29] services using a pub subsystem like
[3:25:31] Reddus so it can scale horizontally and
[3:25:34] include an S3 bucket for media
[3:25:36] attachments. I'll give you a prompt like
[3:25:39] this in the video kit link down in the
[3:25:40] description so you can copy it and paste
[3:25:42] it. But make sure to update the room ID.
[3:25:46] And now let's go ahead and run the test.
[3:25:48] Oh, but before make sure that your dev
[3:25:51] server is connected right here. If it's
[3:25:53] not connected and then we'll be able to
[3:25:55] run the test.
[3:25:57] As you run it, you'll be able to see all
[3:26:00] the information about this specific task
[3:26:03] run. When it was triggered, when it was
[3:26:05] ceued, and when it has started. Now,
[3:26:08] immediately it'll fail after three
[3:26:10] attempts saying that we exceeded our
[3:26:12] current quota, and we need to check our
[3:26:14] Google billing plan. So, it's super
[3:26:16] convenient to be able to test the runs
[3:26:18] directly within the trigger dashboard.
[3:26:20] So once you top it up or change your
[3:26:22] providers, uh you can just reload your
[3:26:24] trigger dev server and then replay the
[3:26:26] run.
[3:26:28] Hopefully this time it continues running
[3:26:31] after just a couple of seconds. And we
[3:26:33] get another little API error saying that
[3:26:35] models Gemini 2.0 flash is no longer
[3:26:38] available. Um I wish they made those
[3:26:41] backwards compatible, but it is what it
[3:26:43] is. We got to find one that actually is
[3:26:46] compatible. So, instead of using 20
[3:26:48] flash, I'll head over into this design
[3:26:51] agent file. That's going to be right
[3:26:53] here. And I'll switch it over to 2.5
[3:26:58] flash. I believe that is the latest
[3:27:00] running model. Then, when you change it,
[3:27:03] don't forget to rerun your server again,
[3:27:06] the trigger dev server by running mpx
[3:27:08] trigger at latestdev. Then, after it
[3:27:12] creates the local worker, go ahead and
[3:27:14] replay the run. Third times the charm or
[3:27:17] apparently not because after about 20
[3:27:19] seconds we got a little error saying no
[3:27:22] object generated response did not match
[3:27:25] the schema.
[3:27:27] So open up a new chat and let's tell it
[3:27:30] something like this. while implementing
[3:27:35] at 23 that's going to be the 23rd design
[3:27:40] spec that we try to do the agent logic
[3:27:44] or rather we can say after implementing
[3:27:46] I try to run a test and then I give it
[3:27:49] some more information that we use for
[3:27:51] the test itself and then pasted the
[3:27:53] error that we got which you can get from
[3:27:55] the web finally we can tell it something
[3:27:57] like analyze trigger.dev dev and
[3:28:00] liblocks best practices analyzed this
[3:28:02] doc and I shared it a link to the doc of
[3:28:06] the generating structure data part
[3:28:08] because so far it generated it just as
[3:28:11] text but what we need to do instead is
[3:28:14] have some kind of a schema that we can
[3:28:16] validate against. So currently it is
[3:28:18] using this output but what we can do is
[3:28:21] use a so-called tool calling approach
[3:28:24] with generate text with a tools object.
[3:28:28] So I'll tell it analyze this docs page
[3:28:31] and the error and then I'll pass some
[3:28:33] additional info which I think is the
[3:28:35] reason for why it's failing. So that
[3:28:37] design agent is failing because generate
[3:28:39] text is being used with output object
[3:28:43] for structured output. That experimental
[3:28:45] API is causing the runtime error. So
[3:28:48] instead replace it with a tool calling
[3:28:50] approach using generate text with a
[3:28:52] tools object. Each canvas action should
[3:28:55] be its own tool. So we have the add
[3:28:58] node, move node and so on. And this way
[3:29:01] it's going to follow the schema
[3:29:02] precisely. So have a message that looks
[3:29:05] like this and send it out.
[3:29:08] This is also a useful approach uh to
[3:29:10] share it a link uh to a specific
[3:29:13] documentation page so that it can do a
[3:29:15] web fetch and figure out how it works.
[3:29:17] Or alternatively, there's also this
[3:29:19] context 7 which is a library of the
[3:29:22] latest documentations that you can
[3:29:24] directly fuse with cursor claude or
[3:29:26] other LLMs. For example, it has the
[3:29:29] latest docs for Nex.js updated 9 hours
[3:29:31] ago. Same thing for React and most
[3:29:35] likely for AI agents as well. There we
[3:29:38] go. AI SDK. This is what we're using.
[3:29:40] So, if we hook this up with our agent,
[3:29:42] and you can do that very easily just by
[3:29:44] copy and pasting this thing right here,
[3:29:46] it would have all the latest docs. But
[3:29:48] let's see what it can do with just the
[3:29:50] URL. And very quickly, the build passes.
[3:29:53] Here's what changed. The output object
[3:29:55] in generate text relies on the model
[3:29:58] emitting a single structured JSON blob,
[3:30:00] but Gemini 2.5 Flash returned a response
[3:30:03] that didn't match the schema, triggering
[3:30:05] the AI no object generated. So in this
[3:30:08] case we're replacing the output with a
[3:30:10] tool approach where each canvas action
[3:30:13] is its own name tool like add node move
[3:30:16] node and so on. So after generation all
[3:30:18] tool calls are collected and then we get
[3:30:21] the final canvas. Okay. So let's go
[3:30:24] ahead and test it out. Back on trigger
[3:30:26] dev we can just replay the run. And in
[3:30:28] about 15 seconds it finished. We got a
[3:30:31] successful output with 11 actions
[3:30:34] applied and a summary of what happened.
[3:30:37] Now, let's make it even better by adding
[3:30:40] another feature spec right here. That's
[3:30:43] going to be 24 AI presence state.md.
[3:30:48] And the goal of this one is to add a
[3:30:51] shared activity indicator so that when
[3:30:54] AI is generating, everyone in the room
[3:30:56] will see it. A status indicator in the
[3:30:59] sidebar as well as a thinking spinner
[3:31:02] cursor and the input will be disabled
[3:31:04] while generation is active. So, let's go
[3:31:06] ahead and run it with the usual message.
[3:31:11] And let's give it a minute. And I sped
[3:31:14] up the process for you, but this one
[3:31:15] definitely took some time, but
[3:31:18] thankfully the build passes cleanly. We
[3:31:21] added some new types for the tasks.ts,
[3:31:24] modified the liblocks config, and added
[3:31:27] the presence cursors. But before we
[3:31:29] actually go ahead and test this out, I
[3:31:31] want to finish the implementation of the
[3:31:33] sidebar so we can test everything we've
[3:31:36] been working on together. So go ahead
[3:31:39] and open up a 25 sidebar chat feed.md
[3:31:45] file. And within this one, the goal is
[3:31:48] to wire up the AI chat libelocks feed
[3:31:51] into the sidebar. See, live feeds are
[3:31:56] realtime message channels. Think of them
[3:31:58] like a group chat that is tied to a
[3:32:00] specific project room. Anyone in that
[3:32:03] room can send a message and everyone
[3:32:06] else can instantly see it. In this case,
[3:32:08] we're using two separate feeds. The AI
[3:32:11] chat feed and the AI status feed. The AI
[3:32:15] status feed is simply for some kind of
[3:32:17] progress signals and AI chat is for the
[3:32:20] actual conversation. This spec handles
[3:32:23] the chat side where users can send
[3:32:25] messages and make them appear across
[3:32:27] every connected client. So let's go
[3:32:29] ahead and run it and I'll speed it up
[3:32:32] for you. And feature 25 is done. Here's
[3:32:35] what was changed across three files.
[3:32:37] First added some additional types. Then
[3:32:40] in the config we extended the feed
[3:32:43] message data with optional chat fields.
[3:32:46] So now it also supports the sender roll
[3:32:49] content and timestamp alongside the
[3:32:51] existing AI status fields. So they both
[3:32:54] coexist under the same type. The key
[3:32:56] addition right here was the chat feed ID
[3:32:59] constant. So now we support the chat
[3:33:02] alongside the status updates as well.
[3:33:05] And finally just one more thing before
[3:33:07] we test it. We have to wire everything
[3:33:10] together. So far this is just the UI. In
[3:33:13] the last couple of prompts, we
[3:33:14] implemented the UI side of things and
[3:33:16] liblocks side of functionality. Just
[3:33:18] before that, we implemented background
[3:33:21] tasks through trigger.dev. But now we
[3:33:24] have to wire it all together. So go
[3:33:27] ahead and open up 26
[3:33:30] design agentfrontend.
[3:33:34] And as I said, the goal here is really
[3:33:37] to connect everything together. We are
[3:33:40] submitting a prompt from the AI sidebar.
[3:33:43] Then we are tracking the status live
[3:33:46] through the use realtime run function.
[3:33:49] We're also showing a status trip while
[3:33:52] the task runs. And we're letting live
[3:33:55] blocks handle the updates of the canvas
[3:33:58] automatically. So let's go ahead and run
[3:34:00] it. And as soon as it is finished, we're
[3:34:03] going to test everything together. And
[3:34:05] in a couple of minutes, definitely much
[3:34:08] faster than it would take me to do all
[3:34:10] of this, feature 26 is done. Again, just
[3:34:14] modify some of the types, modify the
[3:34:17] config to widen it just a bit. And then
[3:34:19] most importantly, the major rework
[3:34:21] happened within the AI sidebar where the
[3:34:24] handle send now actually pushes the user
[3:34:27] message to AI chat calls API endpoint to
[3:34:32] get the run ID and then the token as
[3:34:34] well to get the public token and then
[3:34:36] stores both in state.
[3:34:39] Finally, trigger dev hooks run. We track
[3:34:42] the run and once it reaches a final
[3:34:44] status it pushes the final AI message to
[3:34:46] the AI chat resetting the loading state
[3:34:49] and clearing the presence. So what do
[3:34:51] you say that we head back over to
[3:34:53] localhost 3000 reload the page and
[3:34:56] you'll see a missing access token in
[3:34:58] trigger context o or use API client
[3:35:01] options. We can quickly head back over
[3:35:04] to just localhost 3000 and editor. It is
[3:35:07] possible that that's because of this
[3:35:08] specific project. So I'll create a new
[3:35:11] project now. I'll call it testing AI
[3:35:16] designs
[3:35:18] and create it. And once again, we
[3:35:21] immediately get the missing access token
[3:35:24] in trigger o context or use API client
[3:35:27] options. So there's this handy little
[3:35:30] copy error info click that you can copy
[3:35:33] and then you can directly paste the full
[3:35:35] error right here. when I try to open a
[3:35:38] specific canvas, this is the error that
[3:35:40] I get. And then we can just display that
[3:35:42] error, tell it to analyze it by
[3:35:46] following the best practices from both
[3:35:49] liblocks and trigger.dev and provide me
[3:35:52] your reasoning and idea of what is wrong
[3:35:56] and how to fix it. So something like
[3:35:58] this does I notice when you don't ask it
[3:36:00] to fix it immediately but rather you
[3:36:02] first ask it to analyze it and give you
[3:36:05] the idea of what it would do that's not
[3:36:08] cluttering the context as much and it
[3:36:10] gives you the ability to say whether you
[3:36:13] would like it to execute what it
[3:36:15] suggests or not. So let's see what it
[3:36:17] comes up with and then we can
[3:36:18] potentially execute it. And very quickly
[3:36:21] it was able to figure out the reasoning
[3:36:23] and I believe it actually applied it
[3:36:24] because it was just a couple of lines of
[3:36:26] code. The root cause was that the use
[3:36:29] real-time run performs an eager
[3:36:31] validation check for access token on
[3:36:33] every render and it doesn't wait for a
[3:36:36] connection attempt. So if we pass empty
[3:36:38] string, it's the same as if we don't
[3:36:40] pass it at all. So it immediately throws
[3:36:42] the error on the first render. But
[3:36:45] rather we need to wait and only when
[3:36:47] there's an active run then we need to
[3:36:49] check for the token. So now if we head
[3:36:51] back you can see that we can open up a
[3:36:54] design the new one as well as the old
[3:36:57] one. So now let's go within the new
[3:36:59] project we created and we are ready to
[3:37:03] describe a new system to AI. In this
[3:37:06] case you can really go ahead and type
[3:37:08] anything. I'll write something like
[3:37:10] this. You can also pause your screen and
[3:37:12] write it with me. But the goal here is
[3:37:14] to design a high-scale ecommerce
[3:37:17] back-end architecture including an API
[3:37:20] gateway, a user service with O, a
[3:37:23] product catalog service using a NoSQL
[3:37:25] database, and an order processing system
[3:37:28] that communicates via a message Q. Also,
[3:37:31] don't forget to add a Reddis cache for
[3:37:33] the catalog to handle high traffic. And
[3:37:36] now we can go ahead and click send.
[3:37:40] You can see that Ghost AI is analyzing
[3:37:42] your request in real time right now.
[3:37:46] I'm going to zoom it in. So this is the
[3:37:48] first status that we're seeing. It says
[3:37:50] working right here. And then immediately
[3:37:52] after we were able to see a completed
[3:37:56] product. So in this case, we get the API
[3:37:59] gateway, the user accessing it, browsing
[3:38:03] different products, placing an order
[3:38:05] through the product catalog service, and
[3:38:07] that goes into the message queue. and
[3:38:09] then the order is actually processed. So
[3:38:11] this is a great and pretty detailed
[3:38:14] system architecture diagram and we were
[3:38:16] able to generate it using AI very
[3:38:19] quickly because we already had the
[3:38:21] underlying system for creating different
[3:38:24] nodes and adding labels within the
[3:38:26] elements and the edges and then we just
[3:38:28] created a system that works in the
[3:38:31] background through trigger.dev dev that
[3:38:33] makes use of all of those
[3:38:35] functionalities within the app,
[3:38:37] generates that JSON, and then we just
[3:38:39] slap it onto the canvas. So now that
[3:38:41] everything is working so well, the last
[3:38:43] missing piece of the puzzle is to
[3:38:46] generate the specs. We need to take
[3:38:49] everything that is on the canvas and
[3:38:51] generate a markdown document that we can
[3:38:53] then actually feed into a thinking or
[3:38:57] planning AI agent which is going to make
[3:38:59] it the strongest possible starting point
[3:39:01] for starting to develop any kind of an
[3:39:04] application for real. But the first step
[3:39:06] is now done. It's all about approaching
[3:39:09] the architecture from a planning and
[3:39:11] very detailed way like you are an
[3:39:14] architect really designing a
[3:39:16] specification document. So in the next
[3:39:18] lesson, let's focus on generating that
[3:39:20] spec.
[3:39:23] The flow for generating the spec is
[3:39:25] almost the same pattern as for
[3:39:27] generating the design. A trigger route,
[3:39:30] a background task, and a token route for
[3:39:33] ownership tracking. Then persistence to
[3:39:36] versel blob, and finally a piece of UI
[3:39:39] to then view and download the result.
[3:39:42] Because we've already built this pattern
[3:39:44] once, these specs will move faster. So
[3:39:48] let's go ahead and build it one by one
[3:39:50] by creating a feature spec number 27
[3:39:53] called spec generation flow.md.
[3:39:58] And yeah, as I told you, the goal of
[3:40:01] this one is to build the full backend,
[3:40:04] the trigger route and the trigger.dev
[3:40:07] task that calls Gemini and then
[3:40:09] generates a markdown spec. But most
[3:40:11] importantly, it generates it from the
[3:40:14] canvas state and the chat history. You
[3:40:18] can see that right here. Spec generation
[3:40:20] based on the project ID, room ID, chat
[3:40:24] history, nodes, and edges. No backend
[3:40:27] yet. We just wanted to execute that
[3:40:29] task. So, let's go ahead and run it. 27
[3:40:32] spec already. I'm not sure how to feel
[3:40:35] about it. Is it too high or too low of a
[3:40:37] number? I mean considering what we've
[3:40:40] implemented and what we've done so far
[3:40:42] like a full stack full canvas AI powered
[3:40:46] application with templates and
[3:40:48] everything else we've done. I mean I
[3:40:51] think this would take us months to
[3:40:53] develop manually. And yeah, now that I
[3:40:56] think about it, I'm sure 27 spec files
[3:41:00] is definitely not a lot for this
[3:41:02] production ready application we've
[3:41:04] developed so far. We're very close. So,
[3:41:07] I believe we'll be able to get it done
[3:41:08] in under 30. Let's make it run. In this
[3:41:12] case, it looks like it's actually
[3:41:13] running all three files in parallel.
[3:41:15] This one was actually pretty quick.
[3:41:17] Feature 27 is complete. And the only
[3:41:20] thing we need to check from this one is
[3:41:22] the trigger task called generate spec.
[3:41:25] So, let's head over into that file. And
[3:41:28] you'll notice that it's quite similar to
[3:41:30] design agent. It takes all the schemas,
[3:41:32] it builds the context, returns it all,
[3:41:35] and here's a system prompt saying that
[3:41:37] we are a Ghost AI senior technical
[3:41:40] architect whose job is to generate a
[3:41:42] comprehensive markdown technical
[3:41:45] specification document based on the
[3:41:47] provider architecture canvas and the
[3:41:49] conversation context. And we then give
[3:41:51] it some information on how to structure
[3:41:53] the spec. Finally, we call the schema
[3:41:56] task coming from trigger. Give it an ID,
[3:41:59] the schema of what it needs to do, the
[3:42:02] ability to retry it after specific
[3:42:04] options, and then what is it actually
[3:42:06] running? In this case, we're calling the
[3:42:08] Google generative AI, and asking it to
[3:42:11] generate the spec, build a context,
[3:42:14] generate it in text. Again, we have to
[3:42:17] use 2.5 flash 2.0 is no longer there.
[3:42:21] And then finally it gets the spec and
[3:42:24] returns it. Before we go ahead and test
[3:42:26] it, we have to first implement a couple
[3:42:28] of functionalities and then wire it to
[3:42:30] the sidebar. So go ahead and open
[3:42:33] feature specs and create a unit 28 spec
[3:42:38] persistence
[3:42:39] download MD. The goal of this one is to
[3:42:44] save the generated spec file to versel
[3:42:46] blob. store the URL in project spec
[3:42:49] prisma model and then add a secure
[3:42:52] download route. Basically same Prisma
[3:42:54] metadata plus the blob content pattern
[3:42:57] that we used for the canvas autosave.
[3:42:59] That's how we want to save it. And then
[3:43:01] finally we want to ensure that it's
[3:43:03] downloadable through this specific API
[3:43:06] route. It should authenticate the user,
[3:43:09] verify the access, verify the spec
[3:43:11] belongs to that project, and then fetch
[3:43:14] the file and return it as a downloadable
[3:43:16] markdown file. Go ahead and open this
[3:43:19] with your AI agent. As usual, we'll tell
[3:43:22] it to read the file, update our progress
[3:43:25] tracker, and then implement it exactly
[3:43:27] as specified.
[3:43:29] And while it's doing its job, let's
[3:43:31] quickly check how the progress tracker
[3:43:33] is coming along. I mean, we've
[3:43:35] implemented so many features so far, and
[3:43:37] all of it is here for future developers
[3:43:40] within your team or future agents
[3:43:42] working on the project to check out and
[3:43:44] then continue developing new features on
[3:43:47] top of all the architecture decisions,
[3:43:50] session notes, and more. So, yeah, let's
[3:43:53] see how it approaches this one. And
[3:43:55] feature 28 is done. A summary right here
[3:43:58] is that it added a project spec Prisma
[3:44:01] model with the ID project ID file path
[3:44:04] and created that and it's attached to a
[3:44:07] project. So if we delete it, it's going
[3:44:09] to be deleted as well. Migrations have
[3:44:11] already been applied for us. Uh I love
[3:44:13] agents for doing that automatically. So
[3:44:15] we don't have to run Prisma generate and
[3:44:17] migrate on our own. And finally, it
[3:44:20] updated the generate spec so that after
[3:44:22] the markdown is generated, it uploads it
[3:44:25] to a versel blob. so that we can
[3:44:27] download it later on and this route is
[3:44:30] responsible for that. So now just before
[3:44:33] we test it, we need to wire everything
[3:44:35] together. You know how I like to make
[3:44:37] sure that these spec files are really
[3:44:39] only handling one thing at a time. So in
[3:44:42] 27 we handled the spec generation flow.
[3:44:45] Then we made it persist by storing it
[3:44:47] into versel blob and creating a download
[3:44:50] route. And now finally in 29 spec ui
[3:44:55] integration.mmd
[3:44:57] we are going to wire everything together
[3:44:59] into the specs tab in the AI sidebar
[3:45:03] through a list of generated specs. We
[3:45:05] can have multiple a preview model that
[3:45:07] renders the markdown in case you want to
[3:45:09] preview it in the browser and finally a
[3:45:12] download action to download it on your
[3:45:14] device. So go ahead and run it and let's
[3:45:17] give it some time to implement it. And
[3:45:19] let's let it do its thing. And now that
[3:45:22] feature 29 is fully implemented and the
[3:45:24] build passes, which is important, we'll
[3:45:27] soon be ready to test it out. So there's
[3:45:29] two new backend routes. The first one
[3:45:31] gets access to all the project
[3:45:33] specifications for a specific project
[3:45:36] and then the second one actually creates
[3:45:38] a downloadable markdown text. and the AI
[3:45:42] sidebar got updated so we can test it
[3:45:44] all out. Back within the browser, if you
[3:45:46] now head over to specs and click
[3:45:49] generate spec, you'll notice that at
[3:45:51] least on my end, nothing's happening. On
[3:45:54] your end, it might be working. Maybe
[3:45:56] your agent did a bit of a better job,
[3:45:58] but at least here it's not budging. But
[3:46:01] thankfully, we are getting some errors
[3:46:03] right here within the terminal. So, I'll
[3:46:06] go ahead and copy these errors and tell
[3:46:09] it when I click the generate spec
[3:46:11] button, it doesn't do anything. And this
[3:46:14] is what I see in the terminal. I pasted
[3:46:16] it and then I'll say analyze it and
[3:46:19] provide a solution.
[3:46:21] Refer to trigger.dev and liblock skills
[3:46:25] if needed and press enter.
[3:46:28] I find it that sometimes it's great to
[3:46:30] explicitly mention that it can refer to
[3:46:32] specific skills if you think it's going
[3:46:34] to be useful. Yeah, this definitely took
[3:46:36] some time, but yeah, it says right here
[3:46:40] just to restart your server. It did some
[3:46:43] additional changes, but I think after
[3:46:45] all the changes, it's necessary to just
[3:46:47] reload it. So, that's what I'm going to
[3:46:49] do. Back on localhost 3000, it's going
[3:46:51] to be active.
[3:46:54] Make sure to reload the page and then
[3:46:56] head over to specs. Click generate spec.
[3:47:00] And it is generating. While it is
[3:47:03] actually generating, you can head over
[3:47:05] to trigger.dev under runs and you can
[3:47:08] see generate spec is being executed as
[3:47:11] we speak. So here you can see a bit more
[3:47:13] information on exactly what is
[3:47:15] happening. This is the payload that we
[3:47:16] sent into it. All the different nodes,
[3:47:19] all the information about the
[3:47:20] architecture and more. And it looks like
[3:47:23] it generated it and returned it. So now
[3:47:25] if you head back, you'll be able to see
[3:47:27] a new markdown file that when you click
[3:47:30] on it, it'll be opened within a markdown
[3:47:33] previewer right here in the browser.
[3:47:36] There we go. It's a bit tiny. We can
[3:47:38] definitely increase its width, but yeah,
[3:47:41] I mean, take a look at this. this
[3:47:43] architecture diagram. It was able to
[3:47:45] generate a pretty hefty technical
[3:47:47] specification document that outlines
[3:47:50] this huge system that we can send over
[3:47:52] to our planning agent and start
[3:47:55] developing it. Let's test the download
[3:47:56] functionality as well. I click the
[3:47:58] button and it opened it up. It's a long
[3:48:02] file, but if you've been following along
[3:48:04] with this course, you know that
[3:48:05] specifications have to be long,
[3:48:08] especially if you're creating one spec
[3:48:10] for the entire system. So that's it.
[3:48:13] That's the full Ghost AI feature set
[3:48:15] working end to end. So what do you say
[3:48:18] that we test out the functionalities one
[3:48:20] more time on two separate screens? At
[3:48:22] least right now I'm on two separate
[3:48:24] tabs. So still logged in with the same
[3:48:26] account, but that should be okay. So
[3:48:29] I'll say final test and create a new
[3:48:32] project.
[3:48:34] That project will immediately show up
[3:48:36] right here as well after reloading the
[3:48:39] page. And now we are viewing it from
[3:48:41] both sides.
[3:48:44] Both of us are in the same room and you
[3:48:46] can see my name and cursor pointing to
[3:48:49] different locations.
[3:48:51] Of course, if it were some other people
[3:48:53] right here, you'll be able to see their
[3:48:55] profiles as well. And as soon as I drag
[3:48:58] and drop something, you can see that it
[3:49:00] appears immediately. It also auto zoomed
[3:49:03] in right here. And we can continue
[3:49:05] creating the diagram. You can see it
[3:49:08] happens in real time and that's the
[3:49:11] beauty of live blocks. What we can do
[3:49:13] next is test the AI functionalities. So
[3:49:16] I'll open up the AI window right here.
[3:49:20] And let's go with something simple and
[3:49:22] default like design an e-commerce
[3:49:24] backend. I'll first select all of these
[3:49:27] by holding the shift key and then remove
[3:49:30] them. and design that e-commerce backend
[3:49:34] by sending a new AI chat message. It'll
[3:49:37] start working on it and very quickly
[3:49:41] it'll generate the full UI right here
[3:49:44] and that UI got generated for the other
[3:49:46] user as well. Finally, we can generate
[3:49:49] some specs out of it and of course this
[3:49:51] is happening in the background as a task
[3:49:54] that is being ran on the trigger.dev dev
[3:49:57] side of things or specifically we are
[3:49:59] running an agent in this case Gemini to
[3:50:02] process something but of course you can
[3:50:04] run all sorts of different AI agents
[3:50:06] media processing media generation like
[3:50:08] there's tons of different use cases for
[3:50:10] how trigger can be used and we can
[3:50:12] definitely explore some more of it in
[3:50:14] one of the upcoming videos but yeah the
[3:50:17] spec is here we can preview it download
[3:50:20] it and that's it that is the entire app
[3:50:24] so in the next lesson
[3:50:26] Let's get it deployed.
[3:50:30] Okay, now that the app is complete,
[3:50:32] before we deploy, we need to switch a
[3:50:35] few services from development to
[3:50:37] production. Dev keys are rate limited
[3:50:40] and aren't meant for real traffic. So,
[3:50:43] we have to update live blocks, trigger
[3:50:46] dev, and make sure that every
[3:50:47] environment variable is set correctly in
[3:50:50] Versell. Let's start with live blocks.
[3:50:53] create a new project and call it Ghost
[3:50:56] AI production or something like that and
[3:51:00] set the environment to production. Then
[3:51:03] from the API key section, simply copy
[3:51:06] the public key, head over into
[3:51:08] yourv.local
[3:51:10] and paste it right here. Live public
[3:51:14] key, you can override the development
[3:51:15] one or in case you want to keep it, you
[3:51:17] can just comment it out. But again, make
[3:51:20] sure to add new production ones right
[3:51:23] here. Or at least when we are deploying
[3:51:25] the project on Verscell, you'll have to
[3:51:27] put these new updated ones. So yeah,
[3:51:30] let's go ahead and update it. Uh the
[3:51:32] live blocks public key is going to be
[3:51:34] this new prod key right here. And also
[3:51:38] let's generate a secret key, which you
[3:51:40] can copy and then also override right
[3:51:44] here. Step two is get the trigger dev
[3:51:47] production API keys by heading over to
[3:51:50] the dashboard and then in the top
[3:51:52] selector right here where it says
[3:51:55] environment switch it over from
[3:51:57] development to production. Then from the
[3:52:01] project settings right here under API
[3:52:03] keys go ahead and copy the secret key
[3:52:07] and replace the existing one right here
[3:52:09] under env.
[3:52:11] Once again, I will comment out the
[3:52:13] previous one and just update this one
[3:52:15] that's going to have prod right here in
[3:52:17] the middle. And below the API keys, you
[3:52:20] can head over to general project
[3:52:21] settings and copy the project ref, which
[3:52:24] I believe should be the same. So if you
[3:52:27] duplicate it
[3:52:29] and override it here, you'll see that
[3:52:31] one is actually the same. So we can
[3:52:33] leave it as it is. Now go ahead and copy
[3:52:36] all of your env. And we have to push our
[3:52:39] changes. So run git add dot get commit-m
[3:52:45] finalize the app and prepare it for
[3:52:48] deployment and then run git push. Then
[3:52:52] head over to versel click add a new
[3:52:54] project and just import it from git.
[3:52:57] Once pushed it should have changes a
[3:52:59] couple of seconds ago not a couple of
[3:53:01] hours ago but the reason it says 5 hours
[3:53:04] here is because we've pushed the changes
[3:53:06] to our dev branch. So for them to show
[3:53:09] up on Versell, we first have to push
[3:53:11] them over to the main branch by creating
[3:53:13] a new PR.
[3:53:16] And in this case, there were so many
[3:53:18] changes that we've done, most of which
[3:53:20] are actually agent skills that we
[3:53:22] installed. So there's going to be 1.7
[3:53:25] million lines of code to review. In this
[3:53:28] case, what I'm going to do just to get
[3:53:29] it deployed is I will first fix the
[3:53:32] conflict we have with Copilot. I'll just
[3:53:35] tell it to completely remove the current
[3:53:38] issues.m MD file, which should fix the
[3:53:42] conflict. Obviously, that's because
[3:53:44] we're hoping not to have any more
[3:53:47] issues. It's going to look into it and
[3:53:49] start implementing it right away. And as
[3:53:51] soon as it has been removed, we're ready
[3:53:53] to merge the PR, which means that the
[3:53:57] latest changes under the Ghost AI
[3:53:59] project should be reflected momentarily.
[3:54:01] And after a reload, they'd say just now.
[3:54:05] So we can go ahead and import it and
[3:54:08] immediately add the environment
[3:54:10] variables by pasting all of them into
[3:54:12] this first key and value pair and it'll
[3:54:15] automatically populate all of them. So
[3:54:17] go ahead and scroll down and click
[3:54:19] deploy. Now we've implemented so many
[3:54:22] individual features within this
[3:54:24] application, integrated and wired up so
[3:54:27] many services across front end and
[3:54:29] backend and Prisma databases.
[3:54:32] It would be a miracle if it worked first
[3:54:35] try. So just as I said that in about 8
[3:54:38] seconds the initial build failed saying
[3:54:40] that we can find a full log right here.
[3:54:43] So I'll go ahead and inspect the
[3:54:45] deployment and it looks like it just
[3:54:47] failed on running mpm install. So
[3:54:50] typically when we face an error this
[3:54:52] early with the mpm install most likely
[3:54:55] culprit is going to be the package lock
[3:54:58] json. So what I like to do in this
[3:55:00] situation is just make sure that we are
[3:55:03] on the main branch and we are and we
[3:55:07] want to delete the package lock JSON
[3:55:08] entirely and then push to the main
[3:55:11] without it by running get add dot get
[3:55:14] commit-m
[3:55:16] remove package lock JSON and running get
[3:55:20] push. This is going to push it straight
[3:55:22] over to main which means that it should
[3:55:25] automatically re-trigger another
[3:55:26] deployment. And this time it is building
[3:55:29] past second 8 successfully installing
[3:55:32] the dependencies. So this time we've
[3:55:34] gotten a bit further but it still breaks
[3:55:36] right here on Prisma. Uh this is a
[3:55:40] typical procedure whenever you're
[3:55:41] publishing a NexJS project on Versel
[3:55:45] with Prisma. You also have to add an
[3:55:47] additional script to the package JSON.
[3:55:50] That's going to be right here. Right
[3:55:53] after lint, go ahead and add a post
[3:55:57] install script where you can run prisma
[3:56:00] generate. So once again, you can make
[3:56:03] that change and push it over to the main
[3:56:06] branch.
[3:56:08] As I told you, it's going to be unlikely
[3:56:10] that the build is going to succeed from
[3:56:12] the first try as we've been developing
[3:56:14] this project for so long locally and in
[3:56:17] development version and now we want to
[3:56:19] run it in production. But don't worry,
[3:56:22] we're going to get there. And third
[3:56:24] times the charm because the status is
[3:56:26] now ready and we are live. So go to the
[3:56:30] project overview and visit your URL
[3:56:33] which brings us back to our off and
[3:56:35] homepage at the same time where after
[3:56:38] you sign in, you are redirected to an
[3:56:41] empty project screen or since we already
[3:56:43] logged in with the same account, you can
[3:56:45] find all of your previous projects. This
[3:56:47] means that everything is working exactly
[3:56:50] as it's supposed to, even on the
[3:56:52] deployed version of the application. So,
[3:56:54] congrats. This was a long build and
[3:56:58] quite a different one from the typical
[3:57:00] ones where we manually code everything
[3:57:02] out. So, I want to hear from you. How
[3:57:04] did you like this new approach? Would
[3:57:06] you like to dive even deeper within the
[3:57:08] Agentic course that I'm working on? If
[3:57:11] so, you can join the wait list. And if
[3:57:13] you haven't already, also go ahead and
[3:57:15] download that sixfile context system for
[3:57:18] agentic development that I prepared for
[3:57:20] you alongside this video. That way you
[3:57:22] can use the same system we followed
[3:57:24] along with this build and implement it
[3:57:27] with your future builds. And yeah, huge
[3:57:30] thanks to Trigger for amazing background
[3:57:32] tasks and AI agent functionalities that
[3:57:35] they allow you to add to your app. Also,
[3:57:37] huge thanks to liblocks for allowing us
[3:57:40] to make our applications interactive.
[3:57:42] And finally to Clerk for simplifying
[3:57:45] authentication and user management.
[3:57:47] Thank you not only for sponsoring this
[3:57:49] video but for developing such amazing
[3:57:51] developer tools that I get to share with
[3:57:54] you guys watching this video. That was
[3:57:56] it for this one. I'll see you within
[3:57:59] jsmastery.com
[3:58:00] or if not there within one of the
[3:58:03] upcoming videos on the YouTube channel.
[3:58:05] Once again thank you for watching and
[3:58:08] have a wonderful day.
