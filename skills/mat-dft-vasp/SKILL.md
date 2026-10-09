---
name: mat-dft-vasp
description: Prepare VASP input files, run DFT calculations (locally or remotely via atomate2), and parse VASP output results.
metadata:
  category: [materials]
  venv: [cpu]
---

# mat-dft-vasp

<!-- mcp-tools-note -->
> [!NOTE]
> Steps written `server.tool` are MCP tool calls: `atomate2.run_atomate2_vasp_calculation` is the `run_atomate2_vasp_calculation`
> tool of the `atomate2` server (`mcp__atomate2__run_atomate2_vasp_calculation`, or
> `mcp__plugin_atomistic-skills_atomate2__run_atomate2_vasp_calculation` when installed as a plugin).
> Without a connected server, run the same tools from the shell. Tools named in
> one command share a process, so a model loaded by `load_model` stays loaded:
>
> ```bash
> ${CLAUDE_SKILL_DIR}/../../venv/run cpu python -m src.mcp_server.cli atomate2 run_atomate2_vasp_calculation key=value
> ```

## Goal
To prepare VASP input files (INCAR, POTCAR, KPOINTS, POSCAR) locally for a structure or list of structures, and to parse the resulting VASP output files (`vasprun.xml`, `OUTCAR`) to extract the final energies, forces, stress, and geometries.

> [!TIP]
> **Atomate2 Recommendation**: It is highly recommended to run VASP through the `atomate2` MCP server/tools instead of manually using this skill. `atomate2` natively handles automatic SLURM job submission, dynamic error handling and on-the-fly corrections, automated result parsing, and MongoDB cloud storage.

## Instructions

### Step 1. Prepare VASP Inputs
Use the `prepare_vasp_inputs.py` script to generate local input files from a structure (CIF, XYZ, POSCAR) or a directory of structures.

```bash
${CLAUDE_SKILL_DIR}/../../venv/run cpu python ${CLAUDE_SKILL_DIR}/scripts/prepare_vasp_inputs.py \
    <structure-path> \
    <output-dir> \
    --preset_type matpes-r2scan \
    --calculation_type relaxation
```

Parameters:
- `structure_path`: Path to a single structure or a directory of structures.
- `output_dir`: Location to write the inputs. If `structure_path` is a directory, subdirectories will be created.
- `--preset_type`: Standard VASP presets. Options include `omat`, `mp`, `matpes-pbe`, and `matpes-r2scan`.
- `--calculation_type`: Defaults to `relaxation`. Use `static` for SCF static single-point.

*(Note: Once inputs are generated, you can submit the VASP jobs to an HPC or local cluster. If you instead want to run VASP jobs automatically through Jobflow on configured remote resources, consider using the `atomate2.run_atomate2_vasp_calculation` MCP tool).*

### Step 2. Parse VASP Results
After the VASP calculation has concluded, extract the output data (energy, forces, stress, structure) using `parse_vasp_results.py`. This handles both single directories (containing a `vasprun.xml`) and root directories with multiple subdirectories.

```bash
${CLAUDE_SKILL_DIR}/../../venv/run cpu python ${CLAUDE_SKILL_DIR}/scripts/parse_vasp_results.py \
    <vasp-output-dir> \
    --save_to_file parsed_results.json
```


## Constraints
- **Environments**: The scripts require the `cpu` environment.
- **Parsing Robustness**: The parser requires at a minimum `vasprun.xml` to succeed. `OUTCAR` is read supplementary.
- **POTCARs**: Note that `prepare_vasp_inputs.py` relies on `pymatgen` to write POTCAR files, which requires your `PMG_DEFAULT_FUNCTIONAL` or `.pmgrc.yaml` to point to a valid POTCAR directory.
- **KPOINTS pitfall**: The installed pymatgen's `VaspInput.write_input` may skip writing `KPOINTS` (the script prints it as saved anyway, and `vis.kpoints` stays None). Verify KPOINTS exists after generation; if missing, write the Gamma-centered mesh manually (e.g. `Kpoints.gamma_automatic(lattice, kpts=0.22)` from `pymatgen.io.vasp.outputs`) before submitting.
- **Remote runs**: `mcp__atomate2__run_atomate2_vasp_calculation` is the preferred submission path, but it can only target hosts registered in `~/.config/jobflow-remote/jobflow_remote.yaml` To submit to another cluster, add a worker entry for it there first.

## References
- Kresse, G. & Furthmüller, J., "Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set". *Physical Review B*, 54, 11169. [DOI](https://doi.org/10.1103/PhysRevB.54.11169)

---

**Author:** Bowen Deng
**Contact:** [GitHub @learningmatter-mit](https://github.com/learningmatter-mit)
