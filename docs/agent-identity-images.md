# Agent Identity Images

Felix encourages every agent to carry a small visual identity kit.

## Files

```text
assets/<agent>-mascot.svg
assets/<agent>-image-prompt.md
```

The README should place the image near the title when an image exists.

The image should include the visible agent name or wordmark. Without that instruction, image models often produce a mascot that represents the role but does not identify the agent.

## Copyright-Safe Prompting

Do:

- describe the agent's job
- describe personality traits
- use generic visual metaphors
- ask for original, ownable art
- specify simple README-friendly composition
- ask for the exact agent name as visible readable text

Do not:

- ask for a copyrighted character
- ask for a brand mascot
- ask for a living artist's style
- ask for a near-copy of a movie, game, anime, comic, or logo design
- use protected names as visual references

## Prompt Template

```text
Create an original mascot or identity image for an open-source CLI named <AGENT_NAME>.
Role: <WHAT_THE_AGENT_DOES>.
Personality: <3-5 TRAITS>.
Visual metaphor: <TOOLS, OBJECTS, OR ENVIRONMENT THAT REPRESENT THE WORK>.
Include the exact readable wordmark "<AGENT_NAME>" prominently in the image, either as a top title, badge, label, or nameplate. The agent name must be visible in the final image.
Style: clean modern vector or product illustration, simple shapes, readable at small README size.
Copyright safety: do not resemble existing characters, brand mascots, movie/game/anime designs, living artists' styles, logos, or protected trade dress.
Output should feel new, ownable, and suitable for an open-source README.
```

## Felix Prompt

```text
Create an original friendly repair-helper mascot for an open-source CLI named Felix.
The character is a cheerful builder/maintainer for agent ecosystems, holding a simple hammer and standing beside modular blocks labeled CLI, Wiki, Tasks, Tests, and CI.
Include the exact readable wordmark "Felix" prominently in the image, either as a top title, chest patch, toolkit label, or clean nameplate. The word "Felix" must be visible in the final image.
Style: clean modern vector illustration, warm and practical, public-domain-friendly, no resemblance to any existing cartoon, game, movie, brand mascot, or copyrighted character.
Do not copy any existing movie, game, cartoon, or brand character design. Use a distinct outfit, face, body shape, color palette, and tool design.
Composition: centered mascot with a small agent scaffolding diagram, transparent or light background, readable at small README size. Keep all text short and legible.
```

## Generated Text Check

After generation, inspect the image. If the agent name is absent, misspelled, or illegible, regenerate with a shorter text request such as:

```text
Same image, but add one clean readable title: "<AGENT_NAME>".
```
