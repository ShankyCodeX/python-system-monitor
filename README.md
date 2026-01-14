# python-system-monitor

A lightweight Python system monitor that collects and displays basic system metrics (CPU, memory, disk, network). This repository contains the source code and utilities to run a simple CLI/TUI monitor.

## Features

- Show CPU usage per core and overall
- Show memory and swap usage
- Show disk usage and I/O
- Cross-platform where possible (Linux, macOS, Windows)

## Requirements

- Python 3.8+
- psutil (recommended)

If the repository includes a `requirements.txt` file, install dependencies with:

```bash
python -m pip install -r requirements.txt
```

Alternatively, install the main dependency directly:

```bash
python -m pip install psutil
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ShankyCodeX/python-system-monitor.git
cd python-system-monitor
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the main script (update the filename below if your entrypoint differs):

```bash
python monitor.py
```

If the repository provides a different entrypoint (for example `main.py` or a `cli` module), replace `monitor.py` with the correct filename.

## Development

- Follow standard Python practices.
- Add unit tests in a `tests/` directory.
- Use linters (flake8) and formatters (black) as desired.

## Contributing

Contributions are welcome. Please open an issue or submit a pull request describing your changes.

## License

Add a license file or include a LICENSE in the repository. If you want MIT, add the following in a `LICENSE` file.

---

If you'd like, I can:

- Adjust the README contents to match the project's actual entrypoint and features.
- Create a `requirements.txt` or `LICENSE` file.
- Open a PR with further documentation (README badges, usage examples, screenshots).

Tell me which of the above you'd like me to do next.
