module.exports = {
    types: [
      { value: "✨ feat", name: "✨ feat:\tAdding a new feature" },
      { value: "🐛 fix", name: "🐛 fix:\tFixing a bug" },
      { value: "📝 docs", name: "📝 docs:\tAdd or update documentation" },
      {
        value: "🖌️ style",
        name: "🖌️ style:\tAdd or update styles, ui or ux",
      },
      {
        value: "♻️ refactor",
        name: "♻️ refactor:\tCode change that neither fixes a bug nor adds a feature",
      },
      {
        value: "⚡️ perf",
        name: "⚡️ perf:\tCode change that improves performance",
      },
      {
        value: "🧪 test",
        name: "🧪 test:\tAdding tests cases",
      },
      {
        value: "🚚 chore",
        name: "🚚 chore:\tChanges to the build process or auxiliary tools and libraries such as documentation generation",
      },
      { value: "⏪️ revert", name: "⏪️ revert:\tRevert to a commit" },
      { value: "🚧 wip", name: "🚧 wip:\tWork in progress" },
      {
        value: "👷 build",
        name: "👷 build:\tAdditions or updates to build process",
      },
      {
        value: "💚 ci",
        name: "💚 ci:\tAdditions or updates to the CI",
      },
    ],
  
    scopes: [
      { name: "frontend" },
      { name: "api" },
    ],
  
    allowCustomScopes: true,
    allowBreakingChanges: ["✨ feat", "🐛 fix"],
    subjectLimit: 100,
  };
  