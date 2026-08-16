# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *
import typing


class CommunityDecision(gl.Contract):
    decision: str

    def __init__(self):
        self.decision = "No proposal evaluated yet."

    @gl.public.write
    def evaluate_proposal(self, proposal: str) -> typing.Any:

        def analyze():
            prompt = f"""
You are evaluating a community proposal.

Proposal:
{proposal}

Decide whether this proposal should be APPROVED or REJECTED.

Consider:
1. Is it useful for the community?
2. Is it realistic?
3. Does it provide meaningful value?
4. Is there any obvious harmful or misleading element?

Return ONLY one of:
APPROVED
REJECTED
"""
            return gl.nondet.exec_prompt(prompt).strip()

        result = gl.eq_principle.prompt_comparative(
            analyze,
            principle="""
The final decision must be exactly the same:
APPROVED or REJECTED.

The reasoning may differ between validators,
but the final decision must agree.
"""
        )

        self.decision = result
        return result

    @gl.public.view
    def get_decision(self) -> str:
        return self.decision
