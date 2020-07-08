# Automate Python Testing With GitHub Actions

![](https://github.com/nikhilkumarsingh/python-github-actions-example/workflows/Python%20application/badge.svg)

Example for creating a simple CI/CD pipeline for a Python Project using Github Actions.
![alt text](https://miro.medium.com/max/875/1*LLUe1zzLFFFmnddPAAhxWw.png "")<br/>
###### Quickstart continuous integration using predefined workflows

GitHub now has built-in tools for Continuous Integration: GitHub Actions. You can use these to automate common tasks such as running unit tests or builds. In this article, we will see how to use GitHub Actions to run Python unit tests each time a new commit is made to the repository.

**Best Use**:heavy_check_mark:<br/>

Software test can save you time and money. It can feel like a bit of a hassle, however, and it's not always top of the priority list. Automation is one way to ease the pain — although setting up Continuous Integration (CI) can sometimes feel like a bit too much effort as well, particularly for small projects.
If your code is already hosted on GitHub, Actions makes it very simple to set up and run CI tasks. It has the functionality of dedicated tools such as Travis CI or Jenkins, with fewer interfaces to configure or account credentials to manage. The template Python application workflow is preconfigured to use the popular pytest package, although can be easily customised for other tools. Typically, the workflow is set up to run ‘on push’, so will be triggered each time a commit is pushed to the repository. 
