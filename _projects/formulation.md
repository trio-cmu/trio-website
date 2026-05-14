---
layout: project
permalink: /projects/formulation/
title: Optimal problem formulation 
subtitle: ...closing the loop between solvers and formulation
description: We explore how to automatically design optimization problems for robotics.
image: images/projects/formulation.png
#external_link: https://github.com/
#repo: greenelab/lab-website-template
tags:
  - robotics
  - optimization

order: 4
featured: true
---

## Differentiable global optimization layers

A straightforward way to close the loop between formulation and solvers is to make the solvers differentiable, allowing us to use them as layers in a larger problem including, for example, deep-learned feature extractors. Thanks to our work on SDPRLayers, one can plug global optimization tools into end-to-end learned pipelines and harvest the advantages of certifiable optimization with deep-learned feature extraction and dimensionality reduction. Ongoing collaborations are exploring how to use this tool for a variety of applications, including *global* sensitivity-aware feature learning and optimization landscape shaping and characterization.

## Solver-aware formulation

Our works on KernelSOS and Koopman-inspired methods are also examples of formulation / modeling choices that are made with the solver in mind. In both cases, we choose model classes that are not only accurate but also amenable to global optimization tools. 