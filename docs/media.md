# Launch media

`assets/icon.png` and `assets/banner.png` were generated with OpenAI's built-in ImageGen tool, then resized for repository use. The icon is also bundled with the installable skill. The banner is 1280×640; upload it under repository Settings → Social preview. A README banner alone does not configure that setting.

## Generation prompts

Icon (logo-brand): A refined premium graphic mark for GitHub Viral Launch: a small orange paper-plane folded from a checklist page, three subtle check marks in the fold, upward movement. Warm ivory background, near-black ink and vivid vermilion orange, crisp editorial graphic illustration, memorable at 32px, precise geometry with tactile printed texture. Centered standalone mark, generous padding. No words, letters, Octocat, rocket, or watermark. Square.

Banner (ads-marketing): Professional wide 2:1 banner for GitHub Viral Launch. Premium Swiss editorial design, warm ivory, near-black typography, vivid vermilion accents. Exact headline: “GitHub Viral Launch”. Subtitle: “16 checks. One stronger launch.” An orange paper plane folded from a checklist sheet, sparse black checklist marks and ruled lines suggest preparation becoming momentum. Whitespace, precise typography, generous safe margins. No Octocat, rocket, star counts, fake UI, gradients, or watermark.

## Animation

The eight-second silent video is a method overview, not a recording of a live agent audit. Its labels describe the actual checklist; it does not show invented results. Editable HyperFrames HTML is in `media/launch/`, using the registry's blur-in timing recipe. No HyperFrames dependency is needed to install or use the skill.

With Node.js 22+, FFmpeg, and local rendering prerequisites from HyperFrames:

```bash
cd media/launch
npm run check
npm run dev
# After reviewing the preview:
npm run render -- --output ../../assets/launch.mp4
ffmpeg -i ../../assets/launch.mp4 -vf 'fps=12,scale=960:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse' -loop 0 ../../assets/launch.gif
```

CLI is pinned at HyperFrames 0.9.2. It may need to download browser/rendering assets on first use. The source is available for inspection and modification under the repository's MIT license; upstream HyperFrames retains its own license.
