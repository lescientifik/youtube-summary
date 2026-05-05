---
description: Transcription brute de la vidéo YouTube "DjangoCon 2022 | Quality Assurance in Django - Testing what matters".
video_id: PChaEAIsQls
url: https://youtu.be/PChaEAIsQls?is=Bvi8BdYUPaICjzgI
title: 'DjangoCon 2022 | Quality Assurance in Django - Testing what matters'
author: 'DjangoCon Europe'
language: en
auto_generated: true
duration: 28:40
fetched_on: 2026-05-05
---

# DjangoCon 2022 | Quality Assurance in Django - Testing what matters

**Chaîne :** DjangoCon Europe  
**URL :** https://youtu.be/PChaEAIsQls?is=Bvi8BdYUPaICjzgI  
**Durée :** 28:40

## Transcription

[0:00] hello everyone hello I'll try to speak
[0:03] not so loud uh I'm really happy to be
[0:06] here this is my first Django account as
[0:09] a speaker and I'm really I want to say
[0:12] thank you for the opportunity given
[0:14] so I'm proud of your gift rather slav
[0:17] georgief in English CEO of hacksoft
[0:20] end-to-end software development company
[0:22] we are based in Bulgaria which is the
[0:26] country where the big red arrow is
[0:28] pointing to this is Eastern Europe
[0:31] and a special swipe 22nd of September is
[0:34] actually the national Independence Day
[0:36] of Bulgaria so a quick shout out to all
[0:39] bulgarians listening or watching
[0:46] the goal of this talk is to be practical
[0:49] problematic and actually provide value
[0:51] for you and if someone has something
[0:55] that's meaningful for him or her after
[0:57] the end of this talk then I will be
[0:59] happy so this is the final goal
[1:02] and the context of this talk we have
[1:05] experience with Django projects that
[1:07] were zero percent test covered to 100
[1:11] test covered and also we are building a
[1:13] currently quality assurance teams and
[1:17] we have some context about this topic
[1:22] something really important just like the
[1:24] beautiful city of Porto this talk is
[1:26] going to have a lot of denim relation so
[1:29] we're gonna go up down up down like
[1:31] really into context and then zoom out
[1:35] and look at the bigger picture so we are
[1:38] in the right place for this
[1:40] so quality assurance this is an
[1:43] interesting topic and first we are going
[1:46] to set the stage and give a point of
[1:51] view from like a development point of
[1:53] view we are developers we are developing
[1:55] a new feature and we just want to we are
[1:58] ready and push it to production
[2:01] we are changing an existing feature
[2:03] we're also ready and we want to push it
[2:05] to production and usually if we just do
[2:10] the work say that we are ready and push
[2:13] to production
[2:15] everything is going to be all right
[2:16] usually most of the times but some of
[2:19] the times we are actually as developers
[2:22] the doc in this picture for the dock is
[2:25] okay when production goes down because
[2:28] it has gone down many times if we know
[2:31] what to do but looking outside it's not
[2:35] really okay and uh the first for me
[2:38] definition of quality assurance is the
[2:40] process that helps us not be in the
[2:43] situation as often but we'll see
[2:47] so
[2:49] before pushing to production we need to
[2:51] take extra steps which are make sure the
[2:54] new feature is working as expected make
[2:57] sure the change that we've done is
[2:59] working as expected but also take into
[3:03] account something that sounds bad and
[3:06] it's also a bad culture regression which
[3:08] means this is the the word that we use
[3:11] for but this was working just last week
[3:13] why it's not working right now so we
[3:15] also need to make sure that we are not
[3:17] introducing regressions and accounting
[3:19] for regressions
[3:21] and of course we can do this manually
[3:23] once we're ready we start clicking using
[3:27] a CLI calling kpis whatever the case is
[3:30] and perhaps the first couple of times we
[3:33] can be pretty exhaustive and with
[3:36] confidence say this is okay let's go to
[3:39] production but as we all know doing this
[3:42] manually does not scale well and it also
[3:44] is very prone to human error and
[3:47] exhaustion like I'm not feeling very
[3:49] productive today so let's just say it
[3:52] works and push the production
[3:54] so we end up writing tests
[3:57] like this is this is the main argument
[4:00] for writing tests because doing it
[4:02] manually is not very good
[4:04] and we're now here this was
[4:08] we know that we have to write tests but
[4:10] now the question is what tests do we
[4:11] write we've been to a motivational talk
[4:14] we are now 100 agree that we need to
[4:16] write tests we go home we have a good
[4:19] night's sleep we wake up we open up our
[4:21] computer and let's write tests you're
[4:24] wearing a t-shirt that says tests are
[4:27] best or best
[4:29] but the question is what to test
[4:32] and since we are at djangocon let's look
[4:37] a picture of a typical Django
[4:38] application be it website or just an API
[4:43] it usually has some kind of view or API
[4:46] which works with forms serializer
[4:50] serializers it's really hard work for
[4:53] bulgarians
[4:55] um we might have business logic we might
[4:57] have salary we might have redis
[4:58] third-party Integrations of course Orem
[5:02] working with the database communication
[5:04] database additional framework
[5:06] abstractions also we may build on top of
[5:09] Django so
[5:11] we open up this diagram and we say okay
[5:14] let's write tests and the question is
[5:18] where what to test
[5:20] and as developers we are conditioned at
[5:24] least this is my opinion to think about
[5:26] unit tests when you're learning how to
[5:30] program or going to University or
[5:33] studying computer science it's all about
[5:36] unit tests and unit tests are really
[5:38] great because it's
[5:40] input output everything's passing
[5:43] everything's working so as developers we
[5:46] look at this
[5:48] directed acyclic graph
[5:51] short for DAC and say okay let's pick
[5:55] the leaf nodes and start testing there
[5:57] and usually every project has some sort
[6:01] of utilities module
[6:03] this is a great place to start because
[6:06] it does not depend on many other things
[6:08] from our application and we open up our
[6:11] utility module and it's a computer
[6:13] science 101 again we have a pretty nice
[6:16] function
[6:17] it's a random function no need to look
[6:20] at it in details just unique buy and we
[6:23] are okay how to test this how to
[6:26] approach this with tests and remember of
[6:29] course we are going to write unit tests
[6:32] using the unit test module in Python and
[6:35] this is very important we are in Django
[6:37] context we've started with utilities and
[6:41] the very first test that we write is
[6:42] using the unit test module and I'll call
[6:45] this the pure unit test
[6:47] and the test is whatever input output it
[6:51] passes everything's great
[6:55] we are in a Django project so we might
[6:58] end up writing a utility that looks like
[7:01] this it's a get object wraps around get
[7:04] all get object or 404 catches the
[7:07] exception returns none because it gives
[7:10] a cleaner interface
[7:12] and now in order to test this it's no
[7:16] longer just input output again it's
[7:18] input output but we need more things in
[7:21] order to test it we might need to
[7:24] actually hit the database and actually
[7:25] have a model and the interesting thing
[7:28] here is that it doesn't really matter
[7:31] what the model is we really don't care
[7:33] about the model
[7:34] and we write three test cases the first
[7:38] one is the happy case the second one is
[7:42] nothing's there and the third one is we
[7:45] still want to raise exception if we are
[7:48] trying to get by something that's not
[7:50] unique because this may show us that we
[7:53] have some kind of problem problem in our
[7:56] data model so
[7:58] so far so good
[8:00] still a unit test the difference here is
[8:03] that we are now using the test case from
[8:05] Django and why we're using it because we
[8:08] need Django test framework to do some
[8:10] additional setup for the database we can
[8:13] no longer just rely on the pure unit
[8:16] test module
[8:18] and so far
[8:20] testing utilities it's quite
[8:23] straightforward it really feels good I
[8:26] love writing test for utilities because
[8:28] it's a quick fake feedback loop I'm
[8:32] documenting usage I can then show this
[8:34] to my colleagues and say look how I'm
[8:37] using this and take notes from the test
[8:41] so it's really good
[8:44] back to the diagram
[8:46] the other Leaf node or database we're
[8:50] like okay
[8:51] I know that I need to write tests I know
[8:54] how to write tests I just wrote some
[8:57] tests for utilities so let's just
[8:59] continue Box by box will be fine
[9:02] eventually
[9:03] and we have a model and we write a test
[9:06] like this I'm pretty sure everyone in
[9:08] this room has written a test that looks
[9:11] like this I have a model and I'm
[9:13] basically testing that
[9:17] the jungle RM works
[9:20] it's like this that's give me gives me
[9:22] the information that the RM is actually
[9:25] working the framework that you're using
[9:26] it's working and that's good and the
[9:29] thing is most probably the Django itself
[9:31] has tests like this that make sure that
[9:35] the framework is working it still feels
[9:37] good because we're doing work and we're
[9:39] getting green ticks but not much else
[9:43] and there is an asterisk here because if
[9:46] I am for example testing a more complex
[9:49] multi-database setup and I just need
[9:51] something that hits the database I may
[9:54] write a test like this to test the
[9:56] database setup not the RM models but we
[10:00] are not achieving very much with tests
[10:02] like this DRM is working right
[10:06] and if we follow this approach follow
[10:10] this strategy where we go to the boxes
[10:13] we pick each of the boxes and write
[10:16] tests for it depending on our context
[10:19] we might end up in like a very dense
[10:22] wood and
[10:25] we might uh
[10:28] be in a situation where everything is a
[10:30] unit because we are writing unit tests
[10:33] and we're not very sure once we get to
[10:36] the boxes that depend on other boxes how
[10:39] to approach it we might start our
[10:41] mocking journey and one month late one
[10:44] month later come back and rethink our
[10:46] priorities but the thing is this can
[10:49] generate a lot of busy work
[10:52] and this is busy work that's not
[10:54] achieving actually very much yes we can
[10:57] have tests we can write tests but the
[11:00] end result is we don't know what we've
[11:03] achieved and most probably we haven't
[11:04] achieved much
[11:07] and ideally of course you can say Rado
[11:09] just test Everything 100 disc coverage
[11:12] everything is going to be good
[11:14] that's the ideal case but it's very rare
[11:18] that we are in the ideal case we have to
[11:20] make time we have to have a strategy
[11:22] have a plan so we're not in the ideal
[11:25] case
[11:26] and this is where we want to perhaps
[11:29] start thinking more strategically about
[11:31] the test the tests that we write
[11:36] and ask actually ask the important
[11:39] question because again
[11:43] just going cune it by unit
[11:45] a lot of busy work but if we don't know
[11:48] what we actually want to achieve with
[11:49] those tests it's just busy work and we
[11:53] want to ask the question what do we want
[11:55] to achieve and it usually
[11:57] the answers are around this we want to
[12:01] have more confidence in development
[12:03] meaning
[12:04] develop quicker ship quicker don't have
[12:08] the anxiety that we've changed something
[12:10] and something completely unrelated
[12:13] someplace else is going to break and
[12:15] we're going to end up in the situation
[12:17] with the dog in the room and
[12:19] everything's on fire where again this is
[12:21] fine so we we want to have more
[12:23] confidence we want to catch nasty
[12:25] regressions again this is part of the
[12:27] confidence we want to reduce the thing
[12:30] that's that's a joke like joke term
[12:33] user-driven development which is write
[12:36] the code push to production give it to
[12:37] users and they'll tell you what's not
[12:39] working
[12:41] sometimes we have to do it but we want
[12:43] to reduce it because users want a
[12:45] working piece of software
[12:47] we want to avoid busy work and that's
[12:49] that's the hard part because we are
[12:51] working we are producing code we are
[12:53] having pull requests with a lot of lines
[12:56] in addition yet
[12:58] we're not very sure what we are
[13:00] contributing to
[13:01] and of course we want to remain in
[13:04] Django context and this is very
[13:05] important for this talk because we are
[13:07] at djangocon and we can go one step
[13:10] further to end-to-end testing client
[13:12] with selenium or whatever else you like
[13:15] but we want to remain in Django context
[13:18] let's say we take care of the back end
[13:20] that's it we have no control over the
[13:22] front end so we want to remain in Django
[13:25] context and that's important
[13:27] so
[13:29] how to think more structure
[13:30] strategically about this well our system
[13:33] has cold Pathways like call stack you
[13:37] you cause you call function and then
[13:38] suddenly then our functions get gets
[13:41] called down the road
[13:43] users are hitting those code pathways
[13:46] and usually in a specific state in a
[13:49] specific code pathway we can have an
[13:51] error and when this error occurs
[13:54] things are not good we we want to
[13:58] basically cover for for the case where
[14:00] we have errors
[14:04] this more strategically we will start
[14:06] with tests that cover
[14:09] as many code Pathways as possible with
[14:12] as little tests as possible
[14:16] sounds good
[14:18] if we come back our diagram
[14:21] it's a Django web application and
[14:23] usually it has an entry point either
[14:26] someone submitting a form or someone
[14:29] calling an API
[14:31] and this thing afterwards calls
[14:35] everything else
[14:37] so this looks like a good candidate to
[14:39] start actually testing
[14:41] and if we are to approach
[14:45] tests that hit the API or the view we
[14:49] can start with something like this this
[14:51] is the test case from Django because we
[14:54] need the database
[14:55] and we can start with basically writing
[14:58] the methods the method name doesn't
[15:01] matter really much at least for me you
[15:03] can call it XYZ it's whatever
[15:05] and then in a dark string as you can see
[15:09] we can describe basically a bunch of
[15:12] steps that the user is doing
[15:15] and this is usually usually called the
[15:17] user Journey or a user flow and this is
[15:20] a change in the way we think about our
[15:24] tests because up until now if we're
[15:27] writing unit tests we are thinking about
[15:30] code
[15:32] what
[15:33] do there's but here we're we start
[15:37] thinking about users and let's say we
[15:39] have a bunch of apis that take care of
[15:41] authentication we say
[15:43] with some kind of verification let's say
[15:45] SMS whatever
[15:47] users start verification
[15:49] tries with your own code tries with
[15:51] correct called obtains access token we
[15:54] actually want to see that this access
[15:55] token is working we log out the original
[15:58] access token no longer works like this
[16:01] is a journey and what this journey is
[16:03] going to give me is some kind of
[16:05] confidence that if a user does this I
[16:08] have replicated the actual code Pathways
[16:11] I'm hitting the same called Pathways and
[16:13] I have assertions at the end
[16:15] so we start taking user Journeys and
[16:18] user flows
[16:19] and
[16:20] Ming in
[16:23] is again
[16:24] an example implementation a more
[16:27] exhaustive assertions can be made but
[16:29] they were not fitting very well on
[16:31] slides so that's why I'm just asserting
[16:34] counts
[16:35] [Music]
[16:36] what we can do
[16:37] we can use Faker generate data sent
[16:40] requests assert
[16:42] internal state
[16:47] okay
[16:49] the thing that we can achieve with this
[16:51] approach and I think that's very
[16:53] important and it's a little bit nuanced
[16:55] is we are hitting both framework codes
[16:59] which is Django
[17:01] we are in a way testing that Django
[17:03] works but we are also hitting our
[17:06] business logic or Apple Logic or domain
[17:09] logic code and we are hitting them in an
[17:12] integrated way
[17:14] because we were we can test framework
[17:17] code but only in isolation
[17:19] no use of it but if we test primer code
[17:22] with business logical then we're
[17:24] covering we're basically replicating
[17:26] what the user is doing
[17:28] and a test like test like this is
[17:31] it can look something like this I have
[17:34] just copy pasted everything from my dog
[17:36] string put it in this
[17:39] strangely looking context manager and
[17:42] fill with the actual test implementation
[17:46] and if you're asking what this context
[17:48] manager is doing it's basically
[17:51] a wrapper for
[17:53] sometimes I miss having blocks in Python
[17:55] so I Implement my own block that just
[17:58] wraps around the piece of code just to
[18:01] visually isolate it from the rest so you
[18:04] can achieve something like this
[18:12] an example implementation
[18:14] this is
[18:16] quite a lot of details are going on here
[18:18] we are calling the database constructing
[18:21] payloads
[18:22] sending requests getting responses we
[18:26] can make assertions based on the
[18:28] responses and continuing forward to
[18:32] assert that this specific journey is
[18:34] behaving as we are expecting
[18:37] and this is kind of integration tests
[18:40] kind of behavior driven development I
[18:43] think we can call it both and is going
[18:46] to be correct but
[18:49] we simulate a user Journey while also
[18:52] having the internal State and
[18:54] representation and this is the powerful
[18:56] thing about those tests that take the
[18:59] API and test everything after it
[19:02] and why if we go to Quality Assurance
[19:04] land people there have something that
[19:07] they call test automation Frameworks and
[19:09] they spend quite a lot of time
[19:10] implementing various test automation
[19:12] Frameworks and by doing this we can
[19:15] actually have a test automation frame we
[19:18] can have Django being detest automation
[19:20] framework because
[19:22] if we come back here we are calling
[19:25] again points as end users but we also
[19:27] have direct access to the database I can
[19:30] just make a query and assert some kind
[19:34] of internal State and say okay this is
[19:37] what needs to happen and this is
[19:40] actually good
[19:42] and it's really powerful
[19:45] and again
[19:47] different test
[19:49] we can have a test that
[19:51] given we want to test access token
[19:54] expiry we say given a user
[19:58] new work here
[20:00] user can access all the requiring apis
[20:03] this should be cannot
[20:06] and so what we do we overwrite settings
[20:11] we send requests but the important thing
[20:14] here
[20:15] is the given a user and this is
[20:19] something else that uh we found quite
[20:22] useful to have in those test cases
[20:24] because it reads very well and it gives
[20:28] you a user and the implementation of
[20:31] given a user is totally up to you
[20:35] whatever your tastes are you can
[20:38] replicate API calls so any given is like
[20:43] executing another set of user Journeys
[20:47] you can use factories you can just use
[20:50] Orem code you can use whatever you like
[20:53] and you can return whatever data
[20:56] structure you like and it's just the
[20:58] concept of wrapping
[21:00] the tools and abstractions that you're
[21:02] going to use so you're kind of
[21:04] decoupling from them and just using this
[21:06] given
[21:09] um
[21:10] this kind of notation
[21:13] and later today there's a talk about
[21:16] Factory boys so make sure to come and
[21:20] listen to it that's why I'm not going to
[21:21] cover Factories at all
[21:24] and another thing that we can do with
[21:27] tests that cover as much grout as
[21:29] possible is we can cover even more
[21:31] ground because usually our apps have
[21:34] some kind of tasks integrated into them
[21:38] like celery and we can say for my tests
[21:42] I will run celery in memory
[21:45] I will mock whatever's going outside I
[21:49] don't want to go S3 or whatever sentimos
[21:54] cover even more ground basically
[21:58] replicating going as close as possible
[22:00] to end-to-end tests basically
[22:03] replicating what users are doing
[22:06] and there's a really nice thing that was
[22:09] previously a package
[22:11] and now it's part of uh Django which is
[22:15] capturing commit callbacks because you
[22:17] most likely execute tasks and
[22:20] transaction callbacks so Django is
[22:23] providing the tools for that
[22:25] and
[22:27] if we are to show some kind of a pattern
[22:29] for those kind of tests
[22:32] it's going to look like this given XYZ
[22:35] I want to replicate a user Journey use
[22:39] Django as my test automation framework
[22:42] have access to the internal State cover
[22:45] as much ground as possible
[22:55] you'll say Okay rattle so yeah this
[22:59] looks good but those tests are slow as
[23:02] hell and if I have thousands of those
[23:05] tests
[23:06] the CIA is going to take forever and the
[23:08] truth is yep there are always trade-offs
[23:11] to be made those types of tests can be
[23:14] slower and more heavier than just unit
[23:17] tests and for example if you give me a
[23:21] project with zero percent test coverage
[23:23] that I need to support and maintain most
[23:26] of my effort initially is going to go
[23:30] towards writing those tests because I
[23:33] can write those tests without even
[23:35] knowing what the project is I just need
[23:37] the entry points and I need the user
[23:40] Journeys and then I can start fiddling
[23:42] with it refactoring and doing things
[23:44] with the project
[23:46] but if you for example give me code like
[23:49] this there is a clean method on a model
[23:53] or something else
[23:55] and if I start testing if this is
[23:58] behaving as expected with the heavy API
[24:02] tests
[24:04] doesn't make much sense then again I
[24:07] will be slowed by the type of test that
[24:10] I'm picking
[24:11] and the more focused unit test will do
[24:13] better here
[24:14] so
[24:16] yep again uh this coming back to this
[24:19] diagram
[24:20] and since we are talking uh about
[24:23] quality assurance uh it's a mandatory to
[24:26] include the test pyramid you know talk
[24:28] about quality assurance but since the
[24:30] test permit is quite boring this is the
[24:33] test cake that's why there's a cherry on
[24:35] top so the test pyramid says most of
[24:37] your tests should be unit some
[24:39] integration some end to end we are
[24:42] excluding end-to-end since we are we
[24:43] want to remain in Django land
[24:46] and perhaps this is the most important
[24:48] slide for me for this talk
[24:51] when I approach quality assurance as a
[24:54] developer in a Django project I open up
[24:57] this diagram and try to figure out where
[25:01] am I going to be more towards unit tests
[25:05] where is utilities and business logic
[25:08] Clarity that's decoupled from the
[25:09] database or more towards integration
[25:12] tests with views and apis and business
[25:15] logic layer interacting with the
[25:17] database and there is a gray area in
[25:20] between
[25:22] that can be covered with both pure unit
[25:24] test cases or Django unit test cases
[25:27] depending on what we actually want to
[25:29] test
[25:31] and the example here is if I want to
[25:34] test this validation I don't need to
[25:37] store this model in the database I can
[25:39] just use it in memory it's going to do
[25:41] the work
[25:42] so this is extremely important and it
[25:45] actually answers the question what to
[25:47] test
[25:48] and sadly the answer is it really
[25:52] depends on your context and it's
[25:54] important to have a test plan that's why
[25:57] there's a quality assurance position
[26:00] teams and it's
[26:03] like software engineering but for
[26:07] other parts of the process and it's
[26:09] really it's really important and this
[26:12] can help you navigate where to put your
[26:15] energy where to put your focus and what
[26:17] to test and it's all about
[26:20] which test case you're using this great
[26:22] marker can I use the test case the pure
[26:26] one yes great I will go with it
[26:28] otherwise I will go with the Django test
[26:30] case or something that inherits it
[26:34] and of course quality assurance is quite
[26:37] the broader topic
[26:39] and testing is a part of it but it's no
[26:43] not the entire part of it
[26:45] and the thing is quality assurance can
[26:48] also include developer experience
[26:50] testing software architecture the how
[26:53] you handle deployment
[26:55] how you handle different parts of the
[26:57] process
[26:58] you can you can assure a decent amount
[27:01] of quality on a project without writing
[27:04] a single line of tests
[27:06] and this is really important to know and
[27:08] to think about it's not only tests we as
[27:12] developers we're wired quality assurance
[27:15] go right tests but sometimes we can
[27:18] increase our quality by doing other
[27:21] things
[27:22] for example we've developed for
[27:24] ourselves on Eternal Django style guide
[27:26] which if we follow is going to guarantee
[27:29] a good amount of quality because we know
[27:31] it's working and we have a pattern that
[27:34] that we've been using quite a lot
[27:36] another example for me my pie is a
[27:39] quality assurance tool
[27:40] it can help you catch certain Errors By
[27:45] having type checker same with typescript
[27:49] and of course testing in Django is
[27:52] really fast topic there are tools
[27:55] libraries best practices and you really
[27:58] need to put in the effort and think
[27:59] about how you approach it it's not just
[28:02] write tests for everything but how you
[28:05] write it what you test what's yours what
[28:08] are your resources and how do you want
[28:09] to spend your time
[28:11] and as I mentioned uh the goal of this
[28:16] talk was to be for you practical so I
[28:18] hope I have kindled some kind of fire
[28:20] that you're going to follow up after
[28:22] this and since I have one more minute uh
[28:27] I'm just going to Tweet a bunch of
[28:29] things that I found useful around the
[28:31] topic of quality assurance on Twitter
[28:33] yeah that's it thank you
