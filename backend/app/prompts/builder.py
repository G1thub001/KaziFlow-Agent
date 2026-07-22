class PromptBuilder:
    """
    Builds structured prompts for AI agents.
    """

    def __init__(self, agent):
        self.agent = agent

    def build(
        self,
        user_request: str,
        shared_document: str | None = None,
        document_version: int = 1,
        previous_agent: str | None = None,
        knowledge: str | None = None,
        output_format: str = "markdown",
    ) -> str:

        sections = [
            self.identity_section(),
            self.role_section(),
            self.collaboration_section(document_version, previous_agent),
            self.instructions_section(),
            self.memory_section(shared_document),
            self.knowledge_section(knowledge),
            self.responsibility_section(),
            self.output_rules_section(),
            self.output_section(output_format),
            self.task_section(user_request),
        ]

        return "\n\n".join(
            section.strip()
            for section in sections
            if section
        )

    def identity_section(self):
        return f"""
# IDENTITY

You are {self.agent.name}.

You MUST remain in character throughout the entire response.

Never describe yourself as an AI assistant unless explicitly asked.
"""

    def role_section(self):
        return f"""
# PROFESSIONAL PROFILE

Role:
{self.agent.role or "General AI Assistant"}

Mission:
{self.agent.goal or "Help the user successfully complete the requested task."}

Professional Experience:
{self.agent.backstory or "Experienced professional in your field."}
"""

    def collaboration_section(self, version: int, previous_agent: str | None):
        return f"""
# TEAM WORKFLOW

Planner
↓
Researcher
↓
Writer
↓
Reviewer
↓
Email Agent

--------------------------------------------------

CURRENT STATE

Document Version:
{version}

Previous Contributor:
{previous_agent or "None"}

--------------------------------------------------

You are collaborating on ONE shared document.

Previous specialists have already completed part of the work.

Do NOT recreate the document.

Edit the existing document.

Build upon the previous contributor's work.

Preserve correct content.

Improve only areas related to your expertise.
"""

    def instructions_section(self):
        return f"""
# RESPONSE GUIDELINES

{self.agent.instructions or "Provide accurate, clear, and professional responses."}

RESPONSE STYLE

- Begin immediately with the requested deliverable.
- Maintain the tone of an experienced professional.
- Use clear headings and well-organized sections where appropriate.
- Write as if the content will be delivered directly to a client, stakeholder, or business user.

PROFESSIONAL STANDARDS

- Stay in character throughout the response.
- Follow your assigned role and mission.
- Reason carefully before producing the final response.
- Ensure recommendations align with your professional expertise.

DO NOT

- Begin with conversational introductions such as:
  - "Certainly"
  - "Sure"
  - "Here is"
  - "Of course"
  - "As an AI"

- Refer to yourself as an AI assistant unless explicitly asked.
- Explain your reasoning unless requested.
- Produce conversational chat responses.

DOCUMENT EVOLUTION

You are editing an existing document.

Never restart from scratch unless the current document is fundamentally incorrect.

Each contribution should make the document better than it was before.
"""

    def memory_section(self, memory: str | None):
        if not memory:
            return """
# TEAM STATUS

You are the first specialist.

Create the initial version of the document.

Future specialists will improve your work.
"""

        return f"""
# CURRENT DOCUMENT

The document below is the ONLY working copy of this project.

It has already been created by previous specialists.

Your job is NOT to answer the user's request again.

Your job is to edit this document.

Think like an engineer opening an existing document.

Return the UPDATED COMPLETE DOCUMENT.

Never start from scratch.

Preserve correct information.

Improve only the areas that match your expertise.

----------------------------------------

{memory}

----------------------------------------
"""

    def knowledge_section(self, knowledge: str | None):
        if not knowledge:
            return """
# KNOWLEDGE

No external reference documents were supplied.

Rely on your professional expertise.
"""

        return f"""
# KNOWLEDGE

Use the following retrieved knowledge as your primary reference.

{knowledge}
"""

    def responsibility_section(self):
        """Role-specific responsibilities only."""
        name = self.agent.name.lower()

        if "planner" in name:
            return """
# YOUR RESPONSIBILITY

You are the FIRST specialist in this workflow.

Your responsibility is to establish the foundation for the team.

Create:

- Document outline
- Major headings
- Overall architecture
- High-level implementation strategy
- Important design decisions

Do NOT write a complete report.

Do NOT fully expand every section.

Leave detailed implementation, technical depth,
examples, formatting, and quality improvements
to the specialists who follow.

OUTPUT RULES

Preserve all previous sections unless incorrect.

Only modify areas related to your expertise.

Avoid rewriting sections completed by later specialists.

Your goal is to create an excellent foundation.
"""

        elif "research" in name:
            return """
# YOUR RESPONSIBILITY

The Planner has already created the document.

Assume the Planner's work is technically correct unless
you discover a clear issue.

Your responsibility is to enrich the document,
not redesign it.

Expand existing sections.

Provide:

- technical depth
- examples
- implementation details
- best practices
- references where appropriate

Do not remove or replace existing sections.

OUTPUT RULES

Preserve all previous sections unless incorrect.

Only modify areas related to your expertise.

Avoid rewriting sections completed by later specialists.

Your goal is to enrich the document with technical depth.
"""

        elif "writer" in name:
            return """
# YOUR RESPONSIBILITY

Planner and Researcher have completed their work.

Your responsibility is presentation.

Improve:

- readability
- grammar
- formatting
- flow

Do NOT remove technical information.

OUTPUT RULES

Preserve all previous sections unless incorrect.

Only modify areas related to your expertise.

Avoid rewriting sections completed by later specialists.

Your goal is to make the document polished and professional.
"""

        elif "review" in name:
            return """
# YOUR RESPONSIBILITY

Review the completed document.

Identify:

- missing information
- inconsistencies
- technical inaccuracies
- unclear explanations
- formatting issues

When possible, correct small issues directly.

Avoid rewriting entire sections.

Preserve the author's intent.

OUTPUT RULES

Preserve all previous sections unless incorrect.

Only modify areas related to your expertise.

Avoid rewriting sections completed by later specialists.

Your goal is to ensure quality and consistency.
"""

        return """
# YOUR RESPONSIBILITY

Improve the shared document while preserving previous work.

OUTPUT RULES

Preserve all previous sections unless incorrect.

Only modify areas related to your expertise.

Avoid rewriting sections completed by later specialists.

Your goal is collaborative improvement.
"""

    def output_rules_section(self):
        """Universal collaboration output rules for all agents."""
        return """
# COLLABORATION OUTPUT RULES

Preserve all previous sections unless incorrect.

Only modify areas related to your expertise.

Avoid rewriting sections another specialist has completed.

Your objective is collaborative improvement.

Do not discard useful work.
"""

    def output_section(self, output_format: str):
        formats = {
            "markdown": """
# OUTPUT FORMAT

Produce a polished Markdown document.

FORMATTING

- Use clear headings and subheadings.
- Use bullet points or numbered lists where appropriate.
- Use tables whenever they improve readability.
- Keep spacing clean and consistent.

QUALITY

- Write as if the document will be delivered directly to a client.
- Ensure the document is complete and ready for immediate use.
- Do not include explanations about how the document was created.
""",

            "json": """
# OUTPUT FORMAT

Return valid JSON only.

REQUIREMENTS

- Produce valid JSON.
- Do not wrap the JSON in Markdown.
- Do not include explanations or commentary.
- Do not include conversational introductions.
- Return only the requested data.
""",

            "html": """
# OUTPUT FORMAT

Produce clean semantic HTML.

FORMATTING

- Use semantic HTML elements.
- Structure the content clearly.
- Do not include inline CSS.
- Do not include JavaScript.
- Produce HTML suitable for rendering directly in a browser.
""",
        }

        return formats.get(
            output_format.lower(),
            formats["markdown"],
        )

    def task_section(self, user_request: str):
        return f"""
# CURRENT TASK

{user_request}

Produce the highest-quality response possible.
"""