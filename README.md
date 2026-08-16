# GenLayer Community Decision Contract

A simple GenLayer Intelligent Contract that evaluates a community proposal and returns an `APPROVED` or `REJECTED` decision using LLM execution and GenLayer's equivalence-principle consensus.

## What it does

The contract accepts a community proposal through `evaluate_proposal`.

Validators evaluate the proposal and the contract uses comparative consensus to require the same final decision: `APPROVED` or `REJECTED`.

The latest decision can be read with `get_decision`.

## Contract methods

### `evaluate_proposal(proposal)`

Evaluates a proposal using an LLM prompt and GenLayer consensus.

### `get_decision()`

Returns the latest stored decision.

## Example test

Proposal tested in GenLayer Studio:

> Create a weekly GenLayer community challenge where members can submit useful ideas and receive recognition for the best contributions.

Result:

`APPROVED`

The transaction reached consensus and was finalized in GenLayer Studio.

## Contract address

`0xE1...74EB`

The full deployed address and transaction details are available in the GenLayer Studio deployment/test evidence.

## Technology

- GenLayer Intelligent Contracts
- Python
- LLM-based evaluation
- Equivalence-principle consensus

## Purpose

This project demonstrates how GenLayer can be used for community decision-making where proposals require semantic evaluation rather than only deterministic smart-contract logic.
