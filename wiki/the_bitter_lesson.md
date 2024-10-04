# The Bitter Lesson

[The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) is an essay by computer scientist [Rich Sutton](https://en.wikipedia.org/wiki/Richard_S._Sutton) 
in which he points out that success in AI has come by a "brute force" approach of building bigger ANNs, using more computation, etc, 
rather than through humans manually imbuing an AI with expertise.

Over the short term, say the duration of a typical research project, the amount of computation available is essentially static, so progress can only be achieved by imbuing an AI program with human understanding. But in the slightly longer term, computation available increases massively, leading to greater performance of the same algorithms.

Sutton gives the example of chess:

> In computer chess, the methods that defeated the world champion, Kasparov, in 1997, were based on massive, deep search. At the time, this was looked upon with dismay by the majority of computer-chess researchers who had pursued methods that leveraged human understanding of the special structure of chess. When a simpler, search-based approach with special hardware and software proved vastly more effective, these human-knowledge-based chess researchers were not good losers. They said that ``brute force" search may have won this time, but it was not a general strategy, and anyway it was not how people played chess. These researchers wanted methods based on human input to win and were disappointed when they did not.

Similar patterns hold for Go, computer vision, and speech recognition.

AI researchers keep making the same kind of mistake because it's an appealing mistake (my emphases):

> We have to learn the bitter lesson that building in how we think we think does not work in the long run. 
>The bitter lesson is based on the historical observations that 
>
>(1) AI researchers have often tried to build knowledge into their agents,
>
>(2) this always helps in the short term, and is **personally satisfying to the researcher**, 
>
>but (3) in the long run it plateaus and even inhibits further progress, 
>
>and (4) breakthrough progress eventually arrives by an opposing approach based on scaling computation by search and learning. 
>
>The eventual success is **tinged with bitterness**, and often incompletely digested, because it is success over a favored, human-centric approach. 

Sutton ends:

> The second general point to be learned from the bitter lesson is that the actual contents of minds are tremendously, irredeemably complex; we should stop trying to find simple ways to think about the contents of minds, such as simple ways to think about space, objects, multiple agents, or symmetries. All these are part of the arbitrary, intrinsically-complex, outside world. They are not what should be built in, as their complexity is endless; instead we should build in only the meta-methods that can find and capture this arbitrary complexity. Essential to these methods is that they can find good approximations, but the search for them should be by our methods, not by us. We want AI agents that can discover like we can, not which contain what we have discovered.

## Source code size versus parameters

This is broadly how LLMs are developed. The source code for an LLM might be a few thousand lines of Python, but the training data will be gigabytes,
and the trained model might have 100 billion parameters. 

Let's compare the size of the code to the number of parameters. If the code is 2000 lines each of 30 characters that's 60 kB = 60e3 bytes.
For the parameters, if each parameter is 1 byte, that 1e11 bytes. 1e11/60e3 ~= 2e6

Now let's do the same for the human brain, comparing the genome with the connectome. The genome has 3.2e9 base-pairs , each of which has 4 possibilities so is thus 1/4 of a byte. That's 3.2e9/4 = 8e8 = 800 MB

The connectome has about 100 billion neurons each with an average of 7000 synapses. Assuming a neuron has one weight per synapse, that's 100e9*7e3 = 7e14 weights. Assuming each weight is 1 byte, 7e14 bytes.

Dividing connectome by genome we get 7e14 / 8e8 = 9e5.

So in both cases the information stored in the parameters is about a million times bigger than the information in the program. In both LLMs and the human brain, the complexity comes mostly from interacting with the world and thus learning about it.



