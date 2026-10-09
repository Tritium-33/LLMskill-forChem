# Packaging notes

Source: https://github.com/jinzhezenggroup/computational-chemistry-agent-skills/tree/5c19e75b256d49849574c999b1965d94024ee072/quantum-chemistry/dft-vasp

Original skill tree is unmodified. Packaging and UI metadata are separate additions. License: LGPL-3.0-or-later. This package does not install scientific software, credentials, pseudopotentials or external services. Follow the user’s authorization before installations or job submission. No scientific execution or native Windows validation was performed for this import.

Nested VASP subskills remain in their original tree and are loaded by the parent skill. dpdata-cli and dpdisp-submit are companion skills; uv/uvx and scientific executables are separate dependencies. Shell, envsubst, tmux and scheduler examples may require WSL/Linux. This is editable source redistribution; the included LGPL and GPL terms apply to upstream material, not the repository MIT license.
