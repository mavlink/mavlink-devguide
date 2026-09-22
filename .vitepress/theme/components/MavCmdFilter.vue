<script setup>
// Sticky filter for the MAV_CMD sections generated into en/messages/*.md.
// Progressive enhancement: the generated page is complete without this component.
// Commands are wrapped by the generator in <div class="mav-cmd" data-mission data-command ...>;
// filtering just sets data-mav-cmd-filter on <html> and CSS (style.css) hides non-matching wrappers.
import { ref, onMounted, onBeforeUnmount, nextTick } from "vue";
import { useRoute } from "vitepress";

const FILTERS = [
  { key: "all", label: "All" },
  { key: "mission", label: "Mission" },
  { key: "command", label: "Command" },
  { key: "fence", label: "Fence" },
  { key: "rally", label: "Rally" },
];

const mounted = ref(false); // render nothing until JS is running: no dead control
const active = ref("all");
const shown = ref(0);
const total = ref(0);
const route = useRoute();

const cmds = () => Array.from(document.querySelectorAll(".mav-cmd"));

function updateOutline() {
  // Outline is built by the theme from all headings; hide entries for hidden commands.
  document.querySelectorAll(".VPDocAsideOutline .outline-link").forEach((a) => {
    const id = decodeURIComponent((a.getAttribute("href") || "").slice(1));
    const target = id && document.getElementById(id);
    const wrapper = target && target.closest(".mav-cmd");
    const hide = wrapper && wrapper.hasAttribute("data-hidden");
    a.parentElement.style.display = hide ? "none" : "";
  });
}

function apply(key) {
  active.value = key;
  const root = document.documentElement;
  if (key === "all") root.removeAttribute("data-mav-cmd-filter");
  else root.setAttribute("data-mav-cmd-filter", key);
  const all = cmds();
  let n = 0;
  all.forEach((el) => {
    const hidden = key !== "all" && !el.hasAttribute("data-" + key);
    el.toggleAttribute("data-hidden", hidden);
    if (!hidden) n++;
  });
  total.value = all.length;
  shown.value = n;
  updateOutline();
}

// A link to a command hidden by the filter would land on nothing: reset to "all".
function revealHashTarget() {
  const id = decodeURIComponent(location.hash.slice(1));
  const target = id && document.getElementById(id);
  const wrapper = target && target.closest(".mav-cmd");
  if (wrapper && wrapper.hasAttribute("data-hidden")) {
    apply("all");
    nextTick(() => target.scrollIntoView());
  }
}

onMounted(() => {
  mounted.value = true;
  apply("all");
  window.addEventListener("hashchange", revealHashTarget);
});
onBeforeUnmount(() => {
  window.removeEventListener("hashchange", revealHashTarget);
  document.documentElement.removeAttribute("data-mav-cmd-filter");
});
</script>

<template>
  <div v-if="mounted" class="mav-cmd-filter" role="group" aria-label="Filter commands by where they can be used">
    <span class="mav-cmd-filter-label">Show:</span>
    <button
      v-for="f in FILTERS"
      :key="f.key"
      type="button"
      :class="{ active: active === f.key }"
      :aria-pressed="active === f.key"
      @click="apply(f.key)"
    >
      {{ f.label }}
    </button>
    <span class="mav-cmd-filter-count" aria-live="polite">{{ shown }} of {{ total }}</span>
  </div>
</template>
