# Week 5: Dynamic Analysis

In this lab we will apply the dynamic analysis techniques that we learnt about in class to our own group systems.

## 1. Your target repository

You will need to be able to execute your group system.

If it can be installed via ```pip install``` then you can just do that, and import it where relevant. 

If you are restricting yourselves to a specific commit in your target repository, there are instructions on how to 
install that directory [here](https://www.geeksforgeeks.org/how-to-install-a-python-package-from-a-github-repository/).

Alternatively, you can put this Python notebook into the root directory of your target repository and execute it 
in there.

For all of the code that follows, any references to the CovaSim target system will need to be replaced with references
to your system. In the second code block of ```dynamicAnalysis.pnynb```, you will also need to update the value in
```config[fileNameFilter]``` to reflect the package-name prefix you want to use to make sure that you don't end up 
including lots of irrelevant trace elements.

## 2. Identify an entry-point and input(s)

Start by running your system (without any tracing). Identify the function you need to execute and the inputs that you 
need to supply.

This can be tricky, and depends on your system and its relevant features / use cases.

One natural starting point is to look at the test-cases for the system. You should already have managed to execute these
as part of your system selection process. You can use sys.settrace to trace test executions as easily as any other
execution.

## 3. Run the dynamic analyses on your system.

Answer the following questions. In most cases you will be able to use the code given. Some will require you to add your
own modifications to the source code.

* What classes appear to be particularly close to each other in terms of calls between them?
  * Based on your other analyses of the system so far, are there any indications of Feature Envy?
* Which methods are called most frequently?
* Which classes have the highest Fan-In and Fan-Out?
  * How does this relate to their roles in the system?

Pick a specific feature that appears to be particularly relevant to the core functionality of the system. Pick another
feature that is "adjacent" to that feature (would appear to use lots of the same code), but that you want to distinguish
from it.

Carry out software reconnaissance to home-in on the relevant feature in the code.

What are the most relevant pieces of code you can identify? Which classes are they in? Does this make sense to you from
your understanding of what the classes do?

## 4. Write your findings up as a mini-report

For each of your findings, report your evidence for or against this in ```findings.md```.