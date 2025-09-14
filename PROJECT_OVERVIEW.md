# Cookbook Project Overview

## Introduction
This repository manages an Obsidian-based cookbook and meal planning system. Ingredients and recipes live as Markdown files with YAML front matter that captures metadata needed for planning, costing, and automation.

## 1. Schema & Metadata
### Ingredients
Mandatory fields are:
- `Stock` – whether the ingredient is currently on hand.
- `BoughtCost`, `BoughtSize`, and `PortionSize` – used to calculate serving costs.
- `Cost` – shop-specific price list.
Derived fields include:
- `PotentialMeals` – how many portions a purchase yields.
- `CostPerMeal` – cost of one portion.
Metadata keys use TitleCase (e.g., `BoughtCost`), with plugin-specific `fileClass` in camelCase.

### Recipes
Mandatory fields are:
- `Ingredients` – array of ingredient note links.
- `Time` – one or more meal times (e.g., Breakfast, Dinner).
- `Day` – target day of the week or schedule reference.
Additional fields such as `Cost` and `tags` are optional but recommended.

### Tag Usage
`tags` are free-form for search and organization; other YAML keys are system-critical and should not be renamed without schema updates.

### Derived Values
`PotentialMeals` and `CostPerMeal` are computed from `BoughtCost`, `BoughtSize`, and `PortionSize` via helper scripts.

## 2. Workflows & Automations
- **New notes** are created with QuickAdd templates backed by Templater.
- **Metadata updates** may be performed automatically through scripts; Codex can also suggest manual edits.
- **Shopping lists** combine duplicate ingredients and may include cost estimates.
- **Weekly meal planner** lives as an Obsidian Canvas presenting a tabular schedule.
- **Update frequency**: Dataview queries refresh automatically; Python utilities run manually when needed.

## 3. Plugin Usage
Essential Obsidian plugins:
- Metadata Menu
- QuickAdd
- Templater
- Dataview
Codex should stay within this stack unless new plugins are explicitly approved. Preferred output is basic Dataview tables; DataviewJS is used only when necessary.

## 4. Change Management
- Codex generally provides Markdown snippets for review; direct edits are allowed in trusted mode.
- Maintain a `CHANGE LOG` tracking schema, scripts, and dashboard updates.
- Default approval flow: **Suggestion → Review → Implement**.

## 5. Future Features
- Priorities: nutrition data, ingredient substitutions, and potential export options.
- External integrations are out of scope for now.
- Visualization preference leans toward Dataview tables, with charts considered later.

## 6. Governance & Safety
- Folder structure: ingredient notes in `Ingredients/`, recipes in `Recipe/`.
- Preserve history when merging or deleting fields; use Git commits for rollback.
- Create backups before large schema changes.

