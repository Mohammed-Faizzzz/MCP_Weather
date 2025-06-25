# MCP Weather Application

This is a Python application built using `FastMCP` that interacts with the National Weather Service (NWS) API to provide weather alerts and forecasts. This was a quick project to get used to the MCP Ecosystem, following the [official guide](https://modelcontextprotocol.io/quickstart/server#python).

## Features

  * **Get Weather Alerts:** Retrieve active weather alerts for a specified US state.
  * **Get Weather Forecast:** Obtain a detailed weather forecast for a given latitude and longitude.

## Technologies Used

  * Python 3.11+
  * `httpx`: For making asynchronous HTTP requests to the NWS API.
  * `FastMCP`: A framework for building modular AI tool servers.

## Setup and Installation

Follow these steps to get the project up and running on your local machine.

### 1\. Python Environment

It's highly recommended to use a virtual environment to manage project dependencies. This project requires Python 3.11 or newer.

First, ensure you have `uv` installed (preferably via Homebrew: `brew install uv`).

Navigate to the project's root directory (`MCP_Weather/weather/`):

Create a virtual environment and activate it:

```bash
uv venv
source .venv/bin/activate
```

### 2\. Install Dependencies

With your virtual environment activated, install the required Python packages:

```bash
uv pip install httpx fastmcp
```

### 3\. Configure Your Shell (Important for `uv` and Python)

Based on your setup, it's crucial that your shell correctly prioritizes your desired Python version (e.g., Homebrew Python 3.11.13) and can find the `uv` command.

Ensure that the `conda` initialization lines are completely commented out from your `~/.zshrc`, `~/.zprofile`, and any other shell configuration files (`~/.bashrc`, `~/.bash_profile`, `~/.profile`, `~/.zshenv`).

Also, verify that your `PATH` prioritizes `/opt/homebrew/bin` where `uv` and your Homebrew Python 3.11 are located.

After making any changes to your shell config files, **always close all terminal windows/tabs and open a new one.**

You can verify your Python and `uv` setup with:

```bash
which python3.11
which uv
```

They should point to `/opt/homebrew/bin/python3.11` and `/opt/homebrew/bin/uv` respectively.

## Running the Application

The application runs as an MCP server.

### Via `uv run` (Recommended for Development)

Navigate to the project directory, run the `main.py` script using `uv run`:

```bash
uv run main.py
```

### Via `claude_desktop_config.json`

If you are using this with a Claude desktop application that consumes MCP servers, you would configure it in your `claude_desktop_config.json` (or similar configuration file).

Here's an example configuration for your `mcpServers` block:

```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "ABSOLUTE/PATH/TO/weather",
        "run",
        "main.py"
      ]
    }
  }
}
```

  * **`command`**: Points to the `uv` executable. Ensure this path is correct for your system (`which uv`).
  * **`args`**: Contains the arguments passed to `uv`, including `run`, your script `main.py`, and crucially, explicitly telling `uv` to use your Homebrew Python 3.11.13 interpreter.

### Server Interaction

Once the `FastMCP` server is running (either via `uv run` or your desktop application), it will expose the `get_alerts` and `get_forecast` tools for consumption by your AI agent or other MCP clients. The application is configured to use `stdio` transport, meaning it communicates over standard input/output.

## API Usage

This section describes how an AI agent or client would conceptually use the exposed tools.

### `get_alerts`

Retrieves active weather alerts for a specified US state.

  * **Arguments:**
      * `state` (string): Two-letter US state code (e.g., "CA", "NY").
  * **Example Call (by an AI agent):**
    ```json
    {
      "tool_code": "print(mcp.get_alerts(state='TX'))"
    }
    ```

### `get_forecast`

Retrieves a weather forecast for a given geographical location.

  * **Arguments:**
      * `latitude` (float): Latitude of the location (e.g., 34.05)
      * `longitude` (float): Longitude of the location (e.g., -118.25)
  * **Example Call (by an AI agent):**
    ```json
    {
      "tool_code": "print(mcp.get_forecast(latitude=34.05, longitude=-118.25))"
    }
    ```