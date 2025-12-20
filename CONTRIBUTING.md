# Contributing to Arduino TFT Simulator

First off, thank you for considering contributing to the Arduino TFT Simulator! 🎉

This is a community project and contributions are essential to making it the best TFT simulator for Arduino development.

---

## 📋 Table of Contents

- [How Can I Contribute?](#how-can-i-contribute)
- [Development Priorities](#development-priorities)
- [Development Setup](#development-setup)
- [Code Style Guidelines](#code-style-guidelines)
- [Testing Guidelines](#testing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Bug Reports](#bug-reports)
- [Feature Requests](#feature-requests)
- [Communication](#communication)

---

## 🤝 How Can I Contribute?

### Ways to Contribute

1. **Code Contributions**
   - Implement new TFT_eSPI features
   - Fix bugs
   - Improve performance
   - Add tests

2. **Documentation**
   - Improve README or guides
   - Fix typos or unclear sections
   - Add examples
   - Translate documentation

3. **Testing & Bug Reports**
   - Test with your Arduino sketches
   - Report bugs with detailed info
   - Verify and comment on existing issues

4. **Community Support**
   - Answer questions in Discussions
   - Help other users troubleshoot
   - Share your projects using the simulator

---

## 🎯 Development Priorities

We're focusing on these areas (in order of priority):

### High Priority ⭐⭐⭐
1. **Arduino Font Integration** - `setFreeFont()`, `setFont()` support
   - Parse font files from TFT_eSPI Fonts folder
   - Support GFX fonts
   - Critical for authentic rendering

2. **Sprite Support** - TFT_eSprite class
   - Off-screen rendering buffers
   - Sprite push to main display
   - Essential for complex UIs

3. **Animation Support** - `loop()` execution
   - Execute loop() function repeatedly
   - Timing simulation with `delay()`
   - Frame-by-frame rendering

### Medium Priority ⭐⭐
4. **Touch Input Simulation**
   - Mouse click → touch coordinate mapping
   - Touch event callbacks

5. **Advanced Graphics**
   - `drawArc()`, `fillArc()`
   - `drawEllipse()`, `fillEllipse()`
   - Smooth fonts/anti-aliasing

6. **Color Bitmaps**
   - RGB565/RGB888 bitmap support
   - `pushImage()` function
   - External image loading (.png, .bmp)

### Low Priority ⭐
7. **Performance Optimization**
   - Faster bitmap rendering
   - C/Cython extensions for critical paths

8. **Developer Tools**
   - Live reload on file change
   - Screenshot/video capture
   - Command-line options

---

## 🔧 Development Setup

### Prerequisites

```bash
Python >= 3.7
pygame >= 2.0.0
```

### Setup Steps

1. **Fork the repository**
   - Click "Fork" button on GitHub

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Arduino_TFT_simulator.git
   cd Arduino_TFT_simulator
   ```

3. **Install dependencies**
   ```bash
   pip install pygame
   ```

4. **Test the simulator**
   ```bash
   python tft_simulator_interactive_v2.py main_interface.txt
   python tft_simulator_interactive_v2.py graphic.txt
   ```

5. **Create a branch**
   ```bash
   git checkout -b your-feature-name
   ```

You're ready to code! 🚀

---

## 📝 Code Style Guidelines

### Python Style

- **Follow PEP 8** - Python's style guide
- **Line length**: 100 characters max (flexible to 120 for readability)
- **Naming conventions**:
  - `snake_case` for functions and variables
  - `PascalCase` for classes
  - `UPPER_CASE` for constants

### Code Examples

**Good:**
```python
def drawRect(self, x: int, y: int, w: int, h: int, color: Tuple[int, int, int]):
    """
    Draw a rectangle outline
    
    Args:
        x, y: Top-left corner coordinates
        w, h: Width and height in pixels
        color: RGB tuple (r, g, b)
    """
    pygame.draw.rect(self.surface, color, (x, y, w, h), 1)
```

**Bad:**
```python
def drawRect(self,x,y,w,h,c):  # No docstring, no type hints
    pygame.draw.rect(self.surface,c,(x,y,w,h),1)
```

### Documentation

- **Docstrings**: Add docstrings for all public methods
- **Comments**: Explain "why", not "what"
- **TODO comments**: Use `# TODO: description` for future improvements

### Type Hints

Use type hints where beneficial:
```python
def parse_color(self, color_str: str) -> Tuple[int, int, int]:
    """Parse color string to RGB tuple"""
    ...
```

---

## 🧪 Testing Guidelines

### Manual Testing (Required)

Before submitting a PR, test your changes with:

1. **Provided Examples**
   ```bash
   python tft_simulator_interactive_v2.py main_interface.txt
   python tft_simulator_interactive_v2.py graphic.txt
   ```

2. **Create a Test Sketch**
   - Write a small Arduino sketch that uses your new feature
   - Include it in your PR description
   - Verify output matches expected behavior

3. **Edge Cases**
   - Test with extreme values (0, negative, very large)
   - Test with different rotations (0-3)
   - Test with various colors

### Testing Checklist

- [ ] Tested with `main_interface.txt`
- [ ] Tested with `graphic.txt`
- [ ] Tested with custom sketch (include in PR)
- [ ] No Python errors or warnings
- [ ] Visual output matches expected TFT display
- [ ] Works on different display rotations (if applicable)

### Future: Automated Tests

We plan to add automated tests in the future. Contributions to testing infrastructure are welcome!

---

## 📤 Pull Request Process

### Before Submitting

1. **Update documentation**
   - Update README.md if adding features
   - Update CHANGELOG.md with your changes
   - Add/update guides if needed

2. **Test thoroughly**
   - Follow [Testing Guidelines](#testing-guidelines)
   - Verify no regressions in existing features

3. **Clean commit history**
   - Use clear, descriptive commit messages
   - Squash WIP commits if appropriate

### Submitting Your PR

1. **Push to your fork**
   ```bash
   git push origin your-feature-name
   ```

2. **Open Pull Request**
   - Go to the [original repository](https://github.com/mdmmt05/Arduino_TFT_simulator)
   - Click "New Pull Request"
   - Select your fork and branch

3. **Fill PR Template**
   ```markdown
   ## Description
   Brief description of what this PR does
   
   ## Type of Change
   - [ ] Bug fix (non-breaking change that fixes an issue)
   - [ ] New feature (non-breaking change that adds functionality)
   - [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
   - [ ] Documentation update
   
   ## Testing
   Describe how you tested this. Include:
   - Test sketches used
   - Screenshots/videos (if visual changes)
   - Edge cases tested
   
   ## Example Sketch
   ```cpp
   // Small Arduino sketch demonstrating the new feature
   ```
   
   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Self-reviewed the code
   - [ ] Commented complex sections
   - [ ] Updated documentation
   - [ ] Tested with provided examples
   - [ ] Tested with custom sketch
   - [ ] No errors or warnings

### Review Process

- **All PRs require review** before merging
- Maintainer will review within 1-7 days (usually faster)
- Address review comments by pushing new commits
- Once approved, maintainer will merge

### After Merge

- Your contribution will be credited in:
  - CHANGELOG.md
  - Release notes
  - README acknowledgments (for major contributions)

---

## 🐛 Bug Reports

Found a bug? Help us fix it!

### Before Reporting

1. **Search existing issues** - Bug might already be reported
2. **Try latest version** - Bug might be fixed already
3. **Verify it's a simulator bug** - Not an Arduino code issue

### Creating a Bug Report

**Use the Issue Template:**

```markdown
**Describe the Bug**
Clear description of what's wrong

**To Reproduce**
Steps to reproduce:
1. Run `python tft_simulator_interactive_v2.py test.txt`
2. See error/wrong output

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Arduino Sketch**
```cpp
// Minimal sketch that reproduces the bug
#include <TFT_eSPI.h>
...
```

**Screenshots**
If applicable, add screenshots

**Environment**
- OS: [e.g., Windows 11, Ubuntu 22.04, macOS 13]
- Python version: [e.g., 3.9.7]
- Pygame version: [e.g., 2.5.0]
- Simulator version: [e.g., v2.2]

**Additional Context**
Any other relevant information
```

### Good Bug Reports

✅ **Good**: "drawArc() draws incorrect arc when start angle > end angle"
- Clear, specific, actionable
- Includes minimal reproduction code

❌ **Bad**: "Graphics don't work"
- Too vague, no details, can't reproduce

---

## 💡 Feature Requests

Have an idea? We'd love to hear it!

### Before Requesting

1. **Check existing requests** - It might already be planned
2. **Review [Development Priorities](#development-priorities)**
3. **Consider scope** - Is it TFT simulator related?

### Creating a Feature Request

**Use the Issue Template:**

```markdown
**Feature Description**
Clear description of the feature

**Use Case**
Why is this needed? What problem does it solve?

**Proposed Implementation**
How might this work? (optional)

**Example Code**
```cpp
// How you'd use the feature in Arduino
tft.yourNewFeature(params);
```

**Alternatives Considered**
Other ways to achieve the same goal

**Additional Context**
Screenshots, mockups, references
```

### Feature Priority

Features aligned with [Development Priorities](#development-priorities) will be considered first. Other valuable features may be added to the roadmap.

---

## 📧 Communication

### GitHub Issues & Discussions

**Primary communication channel**: GitHub

- **Issues** - For bugs and specific feature requests
  - [View Issues](https://github.com/mdmmt05/Arduino_TFT_simulator/issues)
  - [Create Issue](https://github.com/mdmmt05/Arduino_TFT_simulator/issues/new)

- **Discussions** - For questions, ideas, and community
  - [View Discussions](https://github.com/mdmmt05/Arduino_TFT_simulator/discussions)
  - [Start Discussion](https://github.com/mdmmt05/Arduino_TFT_simulator/discussions/new)

### Response Time

- **Issues**: Usually reviewed within 1-7 days
- **PRs**: Review within 1-7 days
- **Discussions**: Community-driven, often same-day responses

### Be Respectful

- Be kind and patient
- Assume good intentions
- Provide constructive feedback
- Help others when you can

---

## ⚖️ License

By contributing to Arduino TFT Simulator, you agree that your contributions will be licensed under the MIT License.

- You retain copyright of your contributions
- Your code will be distributed under MIT License
- No CLA (Contributor License Agreement) required

---

## 🏆 Recognition

Contributors will be recognized:

- **CHANGELOG.md** - All contributions listed in releases
- **README.md** - Major contributors acknowledged
- **GitHub** - Automatic contributor listing

Significant contributors may be invited to become maintainers!

---

## ❓ Questions?

Not sure about something?

1. **Read the docs** - Check README, guides, and examples
2. **Search issues** - Question might be answered
3. **Ask in Discussions** - [Start a discussion](https://github.com/mdmmt05/Arduino_TFT_simulator/discussions/new)

---

## 🎉 Thank You!

Every contribution matters - whether it's code, documentation, bug reports, or helping others.

Thank you for helping make Arduino TFT Simulator better! 🚀

---

**Happy coding!** 💻
