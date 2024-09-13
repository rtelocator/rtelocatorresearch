# Neural Run-time Exception Locator

## Introduction

This paper addresses the challenge of localizing runtime exceptions (RTEs) or errors, which represent disruptive
glitches in program execution caused by inherent logic flaws. Unlike traditional fault localization (FL) methods
reliant on code coverage matrices, RTE localization necessitates a specialized approach due to its singular
input responsibility for the exception. We introduce RTE-Locator, an innovative methodology based on
large language models (LLMs), designed to enhance the localization of faults leading to RTEs. Inspired by
manual debugging practices, RTE-Locator emulates the step-by-step execution of statements, with a close
examination of relevant variable values. Leveraging the capability of LLMs to derive values, as well as preconditions
and post-conditions of operations and/or API method calls, RTE-Locator establishes connections
between the observed values, expectations, and the conditions associated with executed statements, allowing
for the identification of inconsistencies and pinpointing of the responsible statement(s).We also leverage LLMs
to automatically fix the fault causing the RTE. Empirical evaluation on real-world datasets demonstrates the
effectiveness of RTE-Locator in achieving high accuracy for RTE localization. In the study on Defects4J, RTELocator
achieved 15.5%, 3.5%, and 2.9% relatively higher in top-1, top-3, and top-5 accuracies, respectively
than the next best state-of-the-art FL approach. We also conducted an experiment to show RTE-Locator’s
usefulness in automated program repair (APR). The combination of RTE-Locator and GPT-4 fixed 8
more bugs (16.3% higher) than the next best baseline APR model when combining with its default fault locator.
