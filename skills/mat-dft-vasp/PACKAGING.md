# Packaging notes

Source: https://github.com/learningmatter-mit/AtomisticSkills/tree/62574443f2a772e23dd5951f3712b65133b06715/skills/mat-dft-vasp

Original skill tree is unmodified. Packaging and UI metadata are separate additions. License: MIT. This package does not install scientific software, credentials, pseudopotentials or external services. Follow the user’s authorization before installations or job submission. No scientific execution or native Windows validation was performed for this import.

The upstream venv/run, src/ backend and atomate2 MCP are not bundled. Resolve scripts relative to this installed skill, and use a separately configured compatible Python environment. Do not treat parser success as convergence: independently check electronic/ionic convergence, interrupted runs and output completeness. Existing project validation and parameter constraints take precedence over upstream defaults.
