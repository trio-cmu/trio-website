---
layout: project
permalink: /projects/seamless/
title: Seamless modeling and optimization
subtitle: ... to lower the barrier of entry to certifiable robotics
image: 
- images/projects/seamless.png
- images/projects/seamless2.png
#external_link: https://github.com/duembgen/popcor
# repo: https://github.com/duembgen/popcor
description: We develop software and tools that automate the process of formulating, solving, and certifying global optimization problems for robotics.
group: featured
order: 3
featured: true
tags:
  - software
---

A persistent theme of our research is to lower the barrier of entry to global optimization for robotics researchers. To this end, we continue to develop software and tools that automate the process of formulating, solving, and certifying global optimization problems for robotics.

## POPCOR

To facilitate the adoption of global optimization tools in robotics, we have developed the software framework Polynomial Optimization for Certifiable Robotics ([POPCOR](https://github.com/duembgen/popcor)). As opposed to existing softwares in the area that are often symbolic in nature, we rely mainly on linear algebra tools to set up problems. This enables us to leverage the powerful linear algebra capabilities of modern computing hardware. 

## GTSAM integration

Many problems in robotics have a graphical structure, where unknown optimization variables are nodes, and edges represent relationships (costs / constraints) between those variables. The software framework [GTSAM](https://gtsam.org/) is a powerful tool for setting up these problems, but to this day the main supported solvers are local in nature. In an ongoing collaboration, we are integrating global optimization tools into GTSAM, greatly improving the accessibility of global optimization for robotics researchers. Conveniently, the core functionalities related to variable elimination and chordal decompositions are already implemented in GTSAM and translate seamlessly to global solvers.