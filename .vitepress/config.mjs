import { defineConfig } from "vitepress";
const getSidebar = require("./get_sidebar.js");

// Tabs: https://github.com/Red-Asuka/vitepress-plugin-tabs
import tabsPlugin from "@red-asuka/vitepress-plugin-tabs";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "MAVLink Guide",
  description: "MAVLink Developer Guide",
  base: process.env.BRANCH_NAME ? "/" + process.env.BRANCH_NAME + "/" : "",

  srcExclude: [
    "de/**/*.md",
    "ja/**/*.md",
    "ru/**/*.md",
    "tr/**/*.md",
    //"ko/**/*.md",
    //"zh/**/*.md",
    "uk/**/*.md",
    "**/_*.md", //Remove source docs that start with "_" (included/not rendered)
  ],
  ignoreDeadLinks: true,
  markdown: {
    math: true,
    config: (md) => {
      // use more markdown-it plugins!
      tabsPlugin(md); //https://github.com/Red-Asuka/vitepress-plugin-tabs
    },
  },
  locales: {
    en: {
      label: "English",
      // other locale specific properties...
      themeConfig: {
        sidebar: getSidebar.sidebar("en"),

        editLink: {
          pattern: ({ filePath, frontmatter }) => {
            if (frontmatter.newEditLink) {
              //newEditLink defines a frontmatter key you can use to append a path to main
              return `https://github.com/mavlink/mavlink-devguide/edit/master/${frontmatter.newEditLink}`;
            } else {
              return `https://github.com/mavlink/mavlink-devguide/edit/master/${filePath}`;
            }
          },
          text: "Edit on GitHub",
        },
      },
    },

    zh: {
      label: "中文 (Chinese)",
      lang: "zh-CN", // optional, will be added  as `lang` attribute on `html` tag
      themeConfig: {
        sidebar: getSidebar.sidebar("zh"),
      },
      // other locale specific properties...
    },
    ko: {
      label: "한국어 (Korean)",
      lang: "ko-KR", // optional, will be added  as `lang` attribute on `html` tag
      themeConfig: {
        sidebar: getSidebar.sidebar("ko"),
      },

      // other locale specific properties...
    },
  },
  //Logs every page loaded on build. Good way to catch errors not caught by other things.
  async transformPageData(pageData, { siteConfig }) {
    console.log(pageData.filePath);
  },

  //

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    siteTitle: false,
    logo: {
      light: "/assets/site/logo_mavlink_header_lightmode.png",
      dark: "/assets/site/logo_mavlink_header_darkmode.png",
      alt: "",
    },
    sidebar: getSidebar.sidebar("en"),
    externalLinkIcon: true,

    editLink: {
      pattern: "https://crowdin.com/project/mavlink",
      text: "Edit translation on Crowdin",
    },

    search: {
      provider: "local",
    },

    nav: [
      {
        text: "Messages",
        link: "/en/messages/common.md",
      },
      {
        text: "FAQ",
        link: "/en/about/faq.md",
      },
      {
        text: "Implementations",
        items: [
          {
            text: "ArduPilot",
            link: "http://ardupilot.org/",
          },
          {
            text: "PX4",
            link: "http://px4.io/",
          },
          {
            text: "Other",
            link: "/en/about/implementations.md",
          },
        ],
      },
      {
        text: "Languages",
        items: [
          {
            text: "C (mavgen)",
            link: "/en/mavgen_c/",
          },
          {
            text: "Python (Pymavlink)",
            link: "/en/mavgen_python/",
          },
          {
            text: "Other",
            link: "/en/#supported_languages",
          },
        ],
      },

      {
        text: "Support",
        link: "/en/about/support.md",
      },
    ],

    socialLinks: [
      { icon: "github", link: "https://github.com/mavlink/mavlink" },
    ],
  },

  head: [
    ["link", { rel: "icon", href: "/en/favicon.ico" }],
    [
      "script",
      {
        async: "",
        src: "https://www.googletagmanager.com/gtag/js?id=G-91EWVWRQ93",
      },
    ],
    [
      "script",
      {},
      `window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-91EWVWRQ93');`,
    ],
  ],

  vue: {
    template: {
      compilerOptions: {
        isCustomElement: (tag) => tag === "lite-youtube",
      },
    },
  },
});
