// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

const site = process.env.SITE_URL;
const base = process.env.SITE_BASE || '/';

export default defineConfig({
	site,
	base,
	integrations: [
		starlight({
			title: 'Skill Bench',
			description:
				'A living research observatory for realistic, diagnostically rich benchmarks of agentic knowledge work.',
			favicon: '/favicon.svg',
			customCss: ['./src/styles/custom.css'],
			social: [
				{
					icon: 'github',
					label: 'Skill Bench on GitHub',
					href: 'https://github.com/incarceron12-cyber/skill-bench',
				},
			],
			head: [
				{
					tag: 'meta',
					attrs: { name: 'theme-color', content: '#08090a' },
				},
			],
			tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 3 },
			sidebar: [
				{
					label: 'Overview',
					items: [
						{ label: 'Research dashboard', slug: '' },
						{ label: 'Project charter', slug: 'charter' },
						{ label: 'Next steps', slug: 'next-steps' },
					],
				},
				{
					label: 'Research synthesis',
					items: [
						{ label: 'Key insights & relevance', slug: 'insights' },
						{ label: 'Benchmark landscape', slug: 'landscape' },
						{ label: 'Landscape research program', slug: 'landscape/research-program' },
						{ label: 'Benchmark methodology', slug: 'methodology' },
					],
				},
				{
					label: 'Paper library',
					items: [{ label: 'Browse by topic', slug: 'papers' }],
				},
				{
					label: 'Operations',
					collapsed: true,
					items: [
						{ label: 'Compounding system', slug: 'operations/compounding-system' },
						{ label: 'Improvement ledger', slug: 'operations/improvement-ledger' },
					],
				},
			],
		}),
	],
});
