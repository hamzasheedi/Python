# 🧽 03_erase_canvas

This project demonstrates an interactive canvas in Python where the user can erase colored blocks by moving a "pink eraser" across them using the mouse.

## 🎮 How It Works

1. A **blue grid** is created on a `400x400` canvas.
2. The program waits for a **click**, which sets the starting position of a **pink eraser box**.
3. As you move your mouse, the pink eraser follows.
4. Any part of the blue grid the eraser touches gets erased (turned white).

## 📐 Features

- Customizable canvas, grid, and eraser sizes.
- Real-time mouse tracking.
- Object collision detection using `canvas.find_overlapping()`.

## 🧠 Concepts Used

- Loops and drawing grids
- Event handling with mouse input
- Object detection and collision logic
- GUI rendering using the `graphics` module

## 🛠 Requirements

- Python 3.x
- `graphics.py` module (or an equivalent canvas-based module)

## ▶️ How to Run

1. Make sure you have the `graphics.py` module installed or placed in the same folder.
2. Save the file as `erase_canvas.py`
3. Run it with:

```bash
python erase_canvas.py
