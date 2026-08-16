# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *
import typing


class CommunityContentReview(gl.Contract):
    result: str

    def __init__(self):
        self.result = "No content reviewed yet."

    @gl.public.write
    def review_content(self, content: str) -> typing.Any:

        def analyze():
            prompt = f"""
You are reviewing a contribution to a Web3 community.

Content:
{content}

Evaluate the content based on:
1. Is it original and meaningful?
2. Does it provide useful information or insight?
3. Is it clear and relevant to the community?
4. Does it avoid obvious spam, misleading claims, or empty promotion?

Return ONLY one of these three labels:

QUALITY
NEEDS_WORK
LOW_QUALITY

Use QUALITY when the contribution is genuinely useful and meaningful.
Use NEEDS_WORK when it has value but needs improvement.
Use LOW_QUALITY when it is mostly spam, empty promotion, or misleading.
"""
            return gl.nondet.exec_prompt(prompt).strip()

        result = gl.eq_principle.prompt_comparative(
            analyze,
            principle="""
The final classification must be exactly the same:
QUALITY, NEEDS_WORK, or LOW_QUALITY.

The reasoning may differ between validators,
but the final classification must agree.
"""
        )

        self.result = result
        return result

    @gl.public.view
    def get_result(self) -> str:
        return self.result
