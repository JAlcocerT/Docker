**KeyStaticCMS**


* https://keystatic.com/docs/introduction

* Thanks to https://github.com/majesticooss/mizar for the working example
    * Forked: https://github.com/JAlcocerT/mizar

* Thanks to https://github.com/Boston343/landingpad
    * https://github.com/JAlcocerT/landingpad

* Thanks to https://github.com/JAlcocerT/barebones-starter for TinaCMS example


---

## Example Setup

```sh
#git clone https://github.com/majesticooss/mizar

cd mizar
npm install
npm run dev --host #as i was using the Opi
npm run build
#npm install -g serve #serve with npm
#serve -s dist #http://localhost:3000
npx serve -s dist #http://localhost:3000

#sudo rm -r .git
```

> http://127.0.0.1:4321/
> > http://127.0.0.1:4321/keystatic or via http://127.0.0.1:4321/admin as per its `astro.config.ts`

---

Keystatic is a “file-based” CMS and rich-content editor that lives alongside your source code.  In practice it gives you:

• A strongly-typed schema (singletons & collections) defined in a single `keystatic.config.ts`
• A local-first (or pluggable) storage layer that writes JSON/Markdown/MDX back into your repo
• A hosted-in-your-dev-server admin UI at /keystatic (and API routes under /api/keystatic)
• Auto-generated TypeScript types for all your content

Because it’s just an Astro integration + filesystem, you can drop it into any Astro SSG project.

Here’s the minimal set-up:

1. Install the packages

```sh
npm install @keystatic/core @keystatic/astro
# or pnpm add -D @keystatic/core @keystatic/astro
```

2. Create `keystatic.config.ts` at your project root:

        import { config, collection, singleton, fields } from "@keystatic/core";

        export default config({
            storage: { kind: "local" },
            ui: { /* optional branding */ },
            singletons: {
            settings: singleton({
                label: "Site Settings",
                path: "src/content/settings",
                format: { data: "json" },
                schema: {
                title: fields.text({ label: "Site Title" }),
                },
            }),
            },
            collections: {
            posts: collection({
                label: "Blog Posts",
                path: "src/content/posts",
                schema: {
                title: fields.text({ label: "Title", validation: { isRequired: true } }),
                body: fields.markdown(),
                },
            }),
            },
        });
        
3. Hook it into your Astro config (`astro.config.ts`):

        import { defineConfig } from "astro/config";
        import keystatic from "@keystatic/astro";
        import keystaticConfig from "./keystatic.config";

        export default defineConfig({
            // …
            integrations: [
            // other integrations…
            keystatic({
                config: "./keystatic.config.ts",
                // optional: route: "/admin"  // custom mount path
            }),
            ],
        });
4. (Optional) If you need to customize the Keystatic UI or icons, you can drop a `.astro/keystatic-imports.js` with:

        import "@keystatic/astro/ui";
        import "@keystatic/astro/api";
        import "@keystatic/core/ui";

    —but in most cases the Astro plugin will scaffold that for you.
5. Run your dev server:

        npm run dev   # defaults to localhost:3000

    – You’ll now have:


    * Admin UI → http://localhost:3000/keystatic

    * API        → http://localhost:3000/api/keystatic

And that’s it.  From there you can:

• Define as many collections/singletons as you like in keystatic.config.ts
• Consume the generated JSON/MDX files in your Astro pages/components
• Commit your content changes right alongside your code

Keystatic works with any static-site setup that can read from the filesystem and mount a Vite dev server (Astro, Vite-only, etc.), but the above is all you need to get it
running in an Astro SSG project.