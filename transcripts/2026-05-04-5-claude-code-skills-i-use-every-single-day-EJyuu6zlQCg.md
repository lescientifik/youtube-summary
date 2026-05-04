---
description: Transcription brute de la vidéo YouTube "5 Claude Code skills I use every single day".
video_id: EJyuu6zlQCg
url: https://youtu.be/EJyuu6zlQCg?is=A8XMAq-r2wnEYpz0
title: '5 Claude Code skills I use every single day'
author: 'Matt Pocock'
language: en
auto_generated: true
duration: 16:42
fetched_on: 2026-05-04
---

# 5 Claude Code skills I use every single day

**Chaîne :** Matt Pocock  
**URL :** https://youtu.be/EJyuu6zlQCg?is=A8XMAq-r2wnEYpz0  
**Durée :** 16:42

## Transcription

[0:00] I've been an engineer for nearly a
[0:01] decade and in all of that time right now
[0:04] process has never been more important.
[0:07] At your fingertips now you have access
[0:08] to a fleet of middling to good engineers
[0:12] that you can deploy at any time. But the
[0:13] weird thing about these engineers is
[0:15] they have no memory. They do not
[0:17] remember things they've done before. And
[0:19] so you need extremely strict and
[0:21] well-defined processes to get those
[0:23] agents to actually do things that are
[0:25] useful. So this means that you as a
[0:27] developer are looking constantly for
[0:29] ways to steer your agents to keep them
[0:31] on the right track. And for me that has
[0:33] resulted in a lot of skill building.
[0:35] Here's the repo of all the skills that
[0:37] I'm using right now. Each of which I
[0:39] have gone through and designed. Some of
[0:40] these I use relatively rarely but some
[0:42] of them I use every single day. And
[0:44] these skills help me encode my process.
[0:46] So the AI has a really strict path it
[0:49] can walk down every single time. And as
[0:51] a result of using all of these skills,
[0:52] the code quality that the AI is
[0:55] producing has shot up. Now, if you think
[0:57] that process is important and that real
[0:59] engineering skills are important, then
[1:01] boy, do I have a course for you. This
[1:02] course is called Claude Code for Real
[1:05] Engineers. It's a 2 week cohort that
[1:07] starts on March 30th and for seven more
[1:10] days, it is 40% off. If you feel like
[1:12] you're behind the curve on Claude Code
[1:14] and you want to get way ahead of the
[1:16] curve in just two weeks, then blime me,
[1:18] this is the place for you. Let's start
[1:19] talking about our skills with number
[1:21] one, which is maybe my favorite. This is
[1:24] the grill me skill. This skill, yes, it
[1:26] is just three sentences long. And let's
[1:28] just read it out in full to describe
[1:30] what it does. Interview me relentlessly
[1:32] about every aspect of this plan until we
[1:34] reach a shared understanding. Walk down
[1:36] each branch of the design tree,
[1:37] resolving dependencies between decisions
[1:39] one by one. And finally, if a question
[1:41] can be answered by exploring the
[1:42] codebase, explore the codebase instead.
[1:44] The concept of a design tree comes from
[1:46] this book by Frederick P. Brooks, which
[1:48] is the design of design. Actually, I
[1:50] don't know if it comes from this book,
[1:51] but this book is where I saw it first.
[1:53] The design tree is this idea that as
[1:55] you're coming towards a design, you need
[1:57] to walk down all of the branches of a
[1:59] design tree. For instance, you might be
[2:01] designing a search page and you need to
[2:02] decide whether you want an advanced
[2:04] search or a text box. If you choose
[2:06] advanced search, then you need to figure
[2:07] out all of the filters and all of the
[2:08] sorting methods that you need on
[2:10] advanced search. and you keep on walking
[2:12] down the tree until you figure out your
[2:14] design kind of in full or as full as you
[2:17] can before actually committing to code.
[2:18] This grill me skill when I invoke it, I
[2:20] invoke it when I want to reach a shared
[2:23] understanding with the LLM. I found that
[2:25] relatively recently claude code will
[2:27] tend to just spit out a plan really
[2:30] early when I go in plan mode and it
[2:31] tends to just create a document before I
[2:34] feel I've reached a shared understanding
[2:35] with the LLM. But the grill me skill
[2:37] forces that conversation. and it forces
[2:39] the LLM to interview me about every
[2:41] single part. Here's a conversation I had
[2:43] with Claude recently about adding a
[2:45] feature to my course video editor
[2:47] codebase. I gave it some research that I
[2:49] done in a markdown file and I said,
[2:50] "Grill me. I'd like to think about
[2:52] adding this to the right page." It
[2:54] loaded up the skill and the thing I want
[2:55] to show you is just how many questions
[2:58] it asked me. So, the first thing it did
[2:59] is it just explored the relevant stuff
[3:01] in the codebase, which is good. Then we
[3:02] zoom down. We can see it asked question
[3:04] one, where does the document live?
[3:06] Question two, what's the UI layout?
[3:07] Question three, which modes get the
[3:09] document panel? Question four, the
[3:10] document life cycle? Question five, what
[3:12] does the right document tool look like?
[3:15] Question six, the edit tool shape.
[3:16] Question seven, question all the way
[3:18] down to question 9. Question 10,
[3:20] question 11, question 12, all the way
[3:22] down to question freaking 16 here. And
[3:25] this is a relatively short grilling
[3:27] session in my book. I've had sessions
[3:29] where I've sat there for nearly half an
[3:31] hour, 45 minutes with the AI answering
[3:33] questions on really complex features.
[3:34] you know, that could be 30, 40, 50
[3:38] questions all from this absolutely tiny
[3:41] skill. That's one thing I want you to
[3:42] take from this. Skills don't have to be
[3:44] long to be impactful. You've just got to
[3:45] choose the right words for the LLM at
[3:47] the right time. And this design tree,
[3:49] resolving dependencies, has just been
[3:51] absolutely great for me. By the way, if
[3:53] you want these skills, then they will be
[3:54] at a link below. Once I have reached a
[3:56] shared understanding with the LLM, once
[3:58] I have grilled my idea and sort of
[4:01] understood all of its ramifications, if
[4:03] I then decide I want to implement it,
[4:05] then I invoke my next skill, which is a
[4:07] write a PRD skill. I actually did this
[4:09] in the conversation we were just looking
[4:10] at. So, it said anything I've missed or
[4:11] got wrong and I said write a PRD. I was
[4:14] suffixing it with user because I have
[4:16] some that sort of live in the project.
[4:18] So, that's the reason why I did that.
[4:19] Here's what the skill looks like. This
[4:20] will be invoked when the user wants to
[4:22] create a PRD. You may skip steps if you
[4:24] don't consider them necessary. So for
[4:25] instance, in the previous conversation,
[4:26] it said, "We've already done a deep
[4:28] interview. Let's move to step four." So
[4:29] step one is to ask the user for a long
[4:31] detailed description. Then number two is
[4:33] to explore the repo to verify their
[4:34] assertions. Number three is basically to
[4:37] interview the user relentlessly. So just
[4:38] a copy of the grill me skill again.
[4:40] Next, we sketch out the major modules
[4:42] you will need to build or modify to
[4:44] complete the implementation. We're going
[4:45] to look at this later because it links
[4:47] to skills I'm going to show you in a bit
[4:49] in this video. And finally, once you
[4:50] have a complete understanding of the
[4:51] problem and the solution, use the
[4:53] template below to write the PRD and the
[4:55] PRD should be submitted as a GitHub
[4:57] issue. The way that my dev flow works is
[4:59] I take these PRDs in GitHub. I turn them
[5:01] into more GitHub issues that reference
[5:03] the parent PRD and then I have a Ralph
[5:07] loop that just loops over each issue
[5:08] until it's done. If we go back to the
[5:10] conversation where we were before, we
[5:11] can see that it created this PRD here.
[5:13] This was 4 days ago. As you can see,
[5:16] we've got a problem statement. The
[5:17] article writing page currently
[5:18] regenerates the entire document on every
[5:20] AI interaction. And the solution was to
[5:22] add a split pane document editing
[5:23] experience to the article writer. Chat
[5:25] stays on the left. A new document panel
[5:26] blah blah blah. So this is a big
[5:27] feature. We're adding document editing
[5:29] to a kind of AI chat feature. The
[5:32] important thing here is the user
[5:33] stories. There are many many user
[5:35] stories as part of this and this comes
[5:36] from agile methodology and we're
[5:38] basically trying to describe the kind of
[5:41] desired behavior of our system in
[5:43] language which is not an easy thing to
[5:44] do. I still haven't properly like landed
[5:46] on the right format for these. This is
[5:48] just something I sort of like, but you
[5:50] could easily use like cucumber language
[5:51] for these or whatever your kind of used
[5:53] to do used to working with. We then zoom
[5:55] down to the bottom and we just sort of
[5:58] pass in some implementation decisions.
[6:00] The implementation decisions here we
[6:02] don't want to be like overprescriptive
[6:04] because we want these to be durable
[6:06] because if the code ends up getting out
[6:08] of date with the PRD, then we're going
[6:09] to have issues when we actually go to
[6:11] implement it. But you can see the theory
[6:12] here. This is the kind of uh it's a
[6:15] really good description of the
[6:16] destination that we're going to. But
[6:18] what we don't have from the PRD is the
[6:20] actual journey is the is the way we're
[6:22] going to get to this destination. And if
[6:24] we leap back to that conversation, this
[6:26] is where I use my next one, which is PRD
[6:29] to issues. What this does is it takes a
[6:31] PRD, takes the destination, and it turns
[6:33] it into a canon board of different
[6:36] issues that can be independently
[6:37] grabbed. So the first step in here is it
[6:39] locates the PRD. If the PD is not
[6:41] already in your context window, fetch it
[6:43] with this instruction. Explore the
[6:44] codebase if you need to. And then
[6:48] draft vertical slices. It's not always
[6:50] clear how you should break a PRD down
[6:53] into individual tasks. This is something
[6:55] that developers have been doing for
[6:57] yonks, right? And we've developed a kind
[6:58] of intuition for how to do it. In my
[7:00] opinion, the best way to do it is to
[7:02] break it into tasks that flush out the
[7:04] unknown unknowns really quickly. For
[7:06] instance, if you're integrating with a
[7:07] new kind of service or integrating two
[7:10] things which you haven't integrated
[7:11] before, then you should do that work
[7:13] first because it's going to give you
[7:14] feedback on whether your approach is
[7:16] even valid. The right analogy here is
[7:18] the tracer bullet analogy. I won't go
[7:19] into what that means, but basically each
[7:21] issue is a thin vertical slice that cuts
[7:23] through all integration layers, not a
[7:26] horizontal slice of one layer. In the
[7:28] conversation, it broke down that really
[7:29] complicated PRD into just four slices.
[7:32] It first created a kind of engine with
[7:34] some tests applied to it. This is
[7:36] actually quite a good vertical slice
[7:37] because this was the engine that was
[7:39] going to then power the rest of the kind
[7:41] of setup. If this engine wasn't working
[7:43] for whatever reason or it wasn't
[7:45] feasible, then we would need to flush
[7:46] that out quickly. And this is what this
[7:48] um breakdown does. The PRD2 issues also
[7:51] establishes blocking relationships
[7:53] between the tasks. For instance, number
[7:55] two here is not actually blocked by
[7:57] anything. So, it can be picked up
[7:58] independently to one. This is really
[8:00] useful if you have a parallel agent
[8:02] setup where you can actually fire two
[8:04] agents at it at once for instance in
[8:06] like background tasks. And it also means
[8:08] that in the future you can add other
[8:10] issues to this like uh QA issues that
[8:12] you find or things that need to be
[8:14] improved. And you can then establish
[8:15] blocking relationships between that and
[8:17] all of the other things. We can see that
[8:18] number three here is blocked by one the
[8:20] editing engine and the number four the
[8:23] Monaco editor toggle is blocked by
[8:25] number two. So I said yes to all of
[8:26] these and it created then all of these
[8:28] GitHub issues. These issues reference
[8:30] the parent PRD so that the uh local
[8:33] agent can fetch it and view it and it
[8:34] sort of just breaks down what to build
[8:36] really and crucially it references the
[8:39] previous user stories in the PRD. We can
[8:41] then see a comment actually from claude
[8:43] code that ended up implementing this. It
[8:45] said a pure function document editing
[8:47] engine with 28 tests covering all
[8:49] acceptance criteria. And we can then
[8:50] take a look at the commit that
[8:51] references this issue. So this was
[8:53] basically my Ralph loop came and just
[8:55] implemented this based on the issue,
[8:56] commented on it, closed it and uh then
[8:59] the next issue was unblocked. So so far
[9:01] the grill me skill can help you flesh
[9:03] out an idea. The write a PRD skill can
[9:06] help you take that idea and turn it into
[9:08] a document and then the PRD is or PRD to
[9:10] issue skill helps you then turn that
[9:13] destination document into an actual
[9:15] journey. But then how do you actually
[9:17] execute on that skill? How do you make
[9:19] it like how do you make the
[9:21] implementation really rock solid and
[9:23] increase the code quality of what gets
[9:24] produced? We have got a TDD skill. TDD
[9:28] means testdriven development. And when
[9:30] you invoke this skill, it basically
[9:32] forces the agent or encourages the agent
[9:34] rather to follow a red green refactor
[9:37] loop. Unusually for my skills, there is
[9:39] actually a lot in here. So it's not just
[9:41] the skill itself. It's also uh ideas on
[9:44] refactoring, on mocking, on what deep
[9:46] modules are. doing really really good.
[9:47] TDD has been the most consistent way
[9:50] that I've improved agents outputs. So
[9:52] let's have a look at what's actually in
[9:54] here. What we can see is I'll just skip
[9:55] over the philosophy stuff. I'll let you
[9:57] guys read that. We are basically looking
[9:59] at this workflow. Yeah. Now the first
[10:01] one here is really important. Confirm
[10:03] with the user what interface changes are
[10:06] needed. Now I made a video on interfaces
[10:07] and implementations recently, but let me
[10:09] just give you the prey. When an AI looks
[10:11] at a bad codebase, it will look at or it
[10:14] will see something like this where it
[10:16] has a ton of tiny modules here that are
[10:18] kind of undifferiated. They're not
[10:20] really grouped together. It doesn't
[10:22] really understand how these things
[10:23] relate. And so it has to do a lot of
[10:25] work kind of working out, okay, what's
[10:27] responsible for what? What are the
[10:28] dependencies? How does this actually
[10:30] how's the codebase even function?
[10:31] Whereas if you restructure this into
[10:33] several larger modules with just kind of
[10:36] thin interfaces on top, the interface
[10:38] being the functions that are actually
[10:40] exported from this, the uh things that
[10:42] the callers actually call, then it's a
[10:45] lot easier for AI to navigate this
[10:46] codebase and it's a lot easier to work
[10:48] out how to test these modules because
[10:50] you just test them at their interfaces.
[10:52] You test them at their boundaries. You
[10:53] can check out the whole video on that
[10:55] below. So what this TDD skill is
[10:56] encouraging here is basically trying to
[10:59] make these interface changes really uh
[11:02] top of mind for the AI to get it to
[11:04] understand that when it changes an
[11:05] interface that's an important decision
[11:07] it needs to take time over. You confirm
[11:09] with the user which behaviors to test.
[11:11] You design the interfaces for
[11:12] testability linking to a dock and then
[11:14] we have some more stuff around planning
[11:16] here. It then goes into a lovely loop
[11:18] where it writes one test at a time and
[11:20] it writes the test first. Now, I've
[11:23] talked about red green refactor before.
[11:24] So, I'll link the video below if you're
[11:26] interested. But I found that red green
[11:27] refactor with agents is incredible, and
[11:30] it basically does this loop until it's
[11:32] complete. It just writes a failing test,
[11:34] then writes the code to make that test
[11:36] pass. Then, finally, it goes through and
[11:37] looks for refactor candidates. I haven't
[11:39] found that this is amazing. It hasn't
[11:42] been brilliant because often LLMs are
[11:45] quite uh you know, they're quite
[11:47] reluctant to refactor their own code. If
[11:49] you were to clear the context of the
[11:50] LLM, then it would just sort of wipe its
[11:52] own memory and it would be a lot less
[11:54] precious about the code that it's just
[11:55] written. But while its own code is
[11:57] sitting in its own context window, it's
[11:59] quite reluctant to change it. So this
[12:00] TDD skill is what I prompt my Ralph
[12:03] loops with in order to get them to do
[12:04] red green refactor. Now TDD demands a
[12:07] lot of you, or rather it demands a lot
[12:09] of your codebase. TDD is really hard to
[12:11] do in a badly structured codebase
[12:14] because the test boundaries of this are
[12:15] really unclear. Should it just sort of
[12:17] test these modules on their own? Should
[12:19] it test these modules on their own? What
[12:21] are the boundaries here? Whereas, when
[12:23] your codebase looks more like this, then
[12:25] it's a lot easier to test because the
[12:27] module boundaries are really clear. So,
[12:28] wouldn't it be great if there was a
[12:30] skill that made your codebase look more
[12:32] like this? Well, isn't it nice? We've
[12:34] got an improve codebase architecture
[12:36] skill. The process for this one is that
[12:37] we explore the codebase and explore it
[12:40] kind of like naturally as an agent
[12:42] would. We're trying to find confusions.
[12:44] We're not like we're trying to sort of
[12:46] surface naturally what the AI finds
[12:48] confusing so that it can then sort of
[12:51] like help it out later. Where does
[12:53] understanding one concept require
[12:54] bouncing around between many small
[12:56] files? Where have pure functions been
[12:58] extracted just for testability, but the
[13:00] real bugs hide in how they're called?
[13:02] Where do tightly coupled modules create
[13:03] integration risk in the seams between
[13:05] them? All of these are questions that a
[13:07] senior engineer would be asking about
[13:09] your codebase. Number two is you present
[13:11] candidates. So you present a numbered
[13:13] list of deepening opportunities. In
[13:15] other words, opportunities to deepen
[13:17] shallow modules in your codebase into
[13:19] deeper ones. The user then picks a
[13:21] candidate and then you design multiple
[13:24] interfaces. So it says to spawn three
[13:27] sub aents in parallel, each of which
[13:29] must produce a radically different
[13:31] interface for the deepen module. In
[13:32] other words, we're extracting that code
[13:34] and designing possible ways that it
[13:36] could look in the future. designing it
[13:38] in multiple different ways is a really
[13:40] great way that you can then decide on
[13:42] the right idea. I've seen this agent
[13:43] spawn like five different sub aents for
[13:45] a really big refactor. The coolest thing
[13:47] about this is you don't need to know a
[13:49] lot about interface design in order to
[13:50] get this working. After comparing, give
[13:52] them your recommendation which design
[13:54] you think is strongest and why. And if
[13:56] elements from different designs would
[13:57] combine well, then propose a hybrid.
[13:59] Notice that I've made this really
[14:01] language agnostic, really kind of sort
[14:04] of everything agnostic really. You can
[14:05] just run this in any codebase and just
[14:07] get a decent answer for how it could be
[14:09] improved. There might be four or five
[14:11] candidates that really could use some
[14:13] work, but really I think you should only
[14:15] be sort of doing one of these at a time
[14:17] because they really are quite hard to
[14:19] get your head around and they require a
[14:21] human in the loop to sit with them and
[14:23] improve the codebase because these
[14:25] decisions do require taste. Finally, it
[14:27] creates a GitHub issue. So, it creates a
[14:29] refactor RFC as a GitHub issue using GH
[14:32] issue create. Usually once this is done,
[14:34] I will then go with my PRD to issues uh
[14:37] skill reference that GitHub issue that's
[14:39] just been created and get it to you know
[14:41] this describes the destination. We then
[14:43] need a journey to get there. So just
[14:45] doing this every so often in a codebase
[14:46] you know once a week just to identify
[14:48] opportunities or if you have a sudden
[14:51] surge of development and you kind of
[14:53] create a whole sort of extra wing of
[14:54] features then this uh skill will be
[14:57] really really useful in just making sure
[14:59] it conforms to the rest of the codebase.
[15:01] making sure that it's not uh too sloppy.
[15:03] And as you keep running this, as you
[15:05] keep refining your codebase, you're
[15:06] going to notice the quality of the
[15:08] agents output goes up. Because the old
[15:10] adage really does apply. If you have a
[15:12] garbage codebase, then the AI is going
[15:13] to produce garbage within that codebase.
[15:15] Because to be honest, if you took all of
[15:17] these skills and just said, "Okay, this
[15:19] is like a little mini markdown book of
[15:21] processes for humans," then it wouldn't
[15:24] look out of place. I found that the most
[15:25] successful way to get code quality up
[15:27] from agents is just to treat them like
[15:30] humans. Humans with weird constraints.
[15:32] Sure, humans that uh have no memory and
[15:34] are just sort of cloned come out of the
[15:36] birthing pod and go right to work. But
[15:38] if you like me think these real
[15:39] engineering skills are super important,
[15:41] then this course is absolutely for you.
[15:44] What I noticed while I was creating the
[15:45] course is that I'm really not teaching
[15:47] Claude code that much. I'm teaching kind
[15:49] of what are sub aents. I'm talking about
[15:51] the constraints of LLMs, the sort of
[15:53] weird smart zone, dumb zone stuff with
[15:55] the context window. We're talking about
[15:57] steering, which is essentially just a
[15:58] way of documenting stuff inside your
[16:00] codebase, how to tackle massive tasks,
[16:03] understanding tracer bullets and
[16:05] building those into our skills,
[16:06] understanding how to build really great
[16:08] feedback loops and doing exercises with
[16:10] them, and crucially, how to hook these
[16:11] up to an autonomous agent. Every part of
[16:14] this course just sort of like leads onto
[16:16] the other, and I'm super happy with how
[16:18] it turned out. So, over the course of
[16:19] two weeks, you'll be working through
[16:21] that self-paced material with me as your
[16:23] guide in Discord and on live office
[16:25] hours. And if that sounds fun to you,
[16:27] then the link is below. Thanks for
[16:28] watching, folks. I'll be coming back
[16:29] with a lot more stuff this week. What
[16:31] would you like me to cover next? I find
[16:33] the intersection between this real
[16:34] engineering and AI is like it's such a
[16:37] awesome place to make content about. But
[16:39] anyway, thanks for watching and I will
[16:40] see you in the next
