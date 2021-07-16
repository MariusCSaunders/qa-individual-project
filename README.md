# Frankendama Sharing

## Contents
* [Introduction](#introduction)
	* [Objective](#objective)
	* [Proposal](#proposal)
* [Architecture](#architecture)
	* [Risk Assessment](#risk-assessment)
	* [Trello Board](#trello-board)
	* [Entity Relationship Diagram](#entity-relationship-diagram)
	* [Test Analysis](#analysis-of-testing)
	* [Continuous Integration](#continuous-integration)
* [Development](#development)
	* [Unit Testing](#unit-testing)
	* [Front-End Design](#front-end)
	* [Integration Testing](#integration-testing)
* [Footer](#footer)

## Introduction

A kendama is a japanese skilltoy that looks like this:
<img src="https://cascadejuggling.com/wp-content/uploads/2020/06/Sweets-Custom-v24-Watermelon-Kendama-1.jpg" alt"A kendama"/>

Which is made up of five parts:
<li>Tama (The ball)</li>
<li>Sarado (The top cups)</li>
<li>Sword (The long part with the spike)</li>
<li>String (Attaches the ball to the ken</li>
<li>Bearing/Bead (Stops the ball coming off the string)</li>

When a user of this toy creates a setup with each 5 parts from different companies, that is called a Frankendama.

### Objective
### Proposal

## Architecture

### Risk Assessment
<img src="https://github.com/MariusCSaunders/qa-individual-project/blob/master/images/RiskAssessment2.png" alt="Risk Assessment"/>
### Trello Board
### Entity Relationship Diagram
My outdated ERD can be seen below, followed by the updated version.
<img src="https://github.com/MariusCSaunders/qa-individual-project/blob/master/images/QAprojectERDdraft1.png" alt="Old ERD"/>
<br/>
My original ERD was a Many-toMany relationship-diagram which is not suitable for this project so i remade the ERD as follows:
<div style="block;"> 
<img align="right" src="https://github.com/MariusCSaunders/qa-individual-project/blob/master/images/QAprojectERDdraft22.png" alt="ERD Image"/>

This is the current ERD for this project.

Each Frankendama will have the 5 main parts for a build and each Frankendama has many companies assosciated to the full build.

### Analysis of Testing
### Continuous Integration
### Jenkins Script

## Development

### Unit Testing
### Front-End
### Integration Testing

## Footer

### Future Improvements
### Author
Marius Saunders
### Acknowledgements
