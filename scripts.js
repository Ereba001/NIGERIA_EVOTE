history.scrollRestoration = 'manual';
window.scrollTo(0, 0);

// Load AOS (Animate On Scroll)
(function() {
    var s = document.createElement('script');
    s.src = 'https://unpkg.com/aos@2.3.1/dist/aos.js';
    s.onload = function() { AOS.init({ duration: 800, easing: 'ease-out-cubic', once: false, offset: 80 }); };
    document.head.appendChild(s);
})();

function createChartOnScroll(id, getConfig) {
    var el = document.getElementById(id);
    if (!el) return;
    var chart = null;
    var seen = false;
    var exited = false;
    function check() {
        var rect = el.getBoundingClientRect();
        if (rect.width === 0 && rect.height === 0) return;
        var inView = rect.top < window.innerHeight && rect.bottom > 0;
        var fullyOut = rect.bottom < 0 || rect.top > window.innerHeight;
        if (inView) {
            if (!chart) {
                chart = new Chart(el, getConfig());
                seen = true;
            } else if (seen && exited) {
                chart.reset();
                chart.options.animation = { duration: 1600, easing: 'easeOutQuart' };
                chart.update();
                exited = false;
            }
        }
        if (fullyOut && seen) {
            exited = true;
        }
    }
    setTimeout(check, 100);
    window.addEventListener('scroll', check);
    window.addEventListener('resize', check);
}

document.addEventListener('DOMContentLoaded', () => {
    /*
    // 0. Theme Toggle (Dark Mode / Light Mode)
    const themeToggle = document.getElementById('themeToggle');
    const STORAGE_KEY = 'evote-theme';

    function getPreferredTheme() {
        const stored = localStorage.getItem(STORAGE_KEY);
        if (stored) return stored;
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }

    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem(STORAGE_KEY, theme);
        if (themeToggle) {
            themeToggle.checked = theme === 'dark';
        }
    }

    // Apply saved or system preference on load
    setTheme(getPreferredTheme());

    // Listen for system preference changes (if user hasn't set a manual preference)
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!localStorage.getItem(STORAGE_KEY)) {
            setTheme(e.matches ? 'dark' : 'light');
        }
    });

    // Toggle on switch change
    if (themeToggle) {
        themeToggle.addEventListener('change', () => {
            setTheme(themeToggle.checked ? 'dark' : 'light');
        });
    }
    */

    var chartAnim = { duration: 1600, easing: 'easeOutQuart' };

    createChartOnScroll('enrollmentChart', function() {
        return {
            type: 'line',
            data: {
                labels: ['Jan','Feb','Mar','Apr','May','Jun'],
                datasets: [{ label:'Voter Registration (Millions)', data:[1.2,1.8,2.5,4.2,3.8,5.5], borderColor:'#008751', backgroundColor:'rgba(0,135,81,0.1)', borderWidth:2, tension:0.4, fill:true, pointBackgroundColor:'#008751', pointRadius:3 }]
            },
            options: { responsive:true, maintainAspectRatio:false, animation:chartAnim, plugins:{ legend:{ display:false } }, scales:{ y:{ beginAtZero:true, max:6.0, ticks:{ stepSize:1, color:'#9ca3af' }, grid:{ color:'#f3f4f6' }, border:{ display:false } }, x:{ ticks:{ color:'#9ca3af' }, grid:{ display:false }, border:{ display:false } } } }
        };
    });

    createChartOnScroll('distributionChart', function() {
        return {
            type: 'pie',
            data: { labels:['North','South','East','West'], datasets:[{ data:[45,20,15,20], backgroundColor:['#008751','#1f2937','#9ca3af','#e5e7eb'], borderWidth:0 }] },
            options: { responsive:true, maintainAspectRatio:false, animation:chartAnim, plugins:{ legend:{ display:false }, tooltip:{ callbacks:{ label:function(c){ return c.label+': '+c.raw+'%'; } } } } }
        };
    });

    createChartOnScroll('liveResultsChart', function() {
        return {
            type: 'pie',
            data: { labels:['Candidate A','Candidate B','Others'], datasets:[{ data:[42,38,20], backgroundColor:['#008751','#2563eb','#9ca3af'], borderWidth:0 }] },
            options: { responsive:true, maintainAspectRatio:false, animation:chartAnim, plugins:{ legend:{ display:false }, tooltip:{ callbacks:{ label:function(c){ return c.label+': '+c.raw+'%'; } } } } }
        };
    });

    createChartOnScroll('identityStatusChart', function() {
        return {
            type: 'line',
            data: { labels:['08:00','09:00','10:00','11:00','12:00'], datasets:[{ data:[30,45,62,55,40], borderColor:'#9ca3af', backgroundColor:'rgba(156,163,175,0.22)', borderWidth:2, tension:0.35, fill:true, pointRadius:3, pointBackgroundColor:'#9ca3af' }] },
            options: { responsive:true, maintainAspectRatio:false, animation:chartAnim, plugins:{ legend:{ display:false } }, scales:{ y:{ min:20, max:70, ticks:{ color:'#9ca3af' }, grid:{ display:false }, border:{ display:false } }, x:{ ticks:{ color:'#9ca3af' }, grid:{ display:false }, border:{ display:false } } } }
        };
    });

    var counters = document.querySelectorAll('.counter');
    if (counters.length) {
        var counterObs = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (!entry.isIntersecting) return;
                var el = entry.target;
                el.textContent = '0';
                var target = parseFloat(el.dataset.target);
                var suffix = el.dataset.suffix || '';
                var duration = 2000;
                var start = performance.now();
                var decimals = (target % 1 === 0) ? 0 : String(target).split('.')[1].length;
                function tick(now) {
                    var progress = Math.min((now - start) / duration, 1);
                    var eased = 1 - Math.pow(1 - progress, 4);
                    el.textContent = (decimals ? (eased * target).toFixed(decimals) : Math.floor(eased * target)) + suffix;
                    if (progress < 1) requestAnimationFrame(tick);
                }
                requestAnimationFrame(tick);
            });
        }, { threshold: 0.5 });
        counters.forEach(function(c) { counterObs.observe(c); });
    }

    var nav = document.querySelector('.navbar');
    if (nav) {
        var shrinkCheck = function() {
            nav.classList.toggle('navbar-shrink', window.scrollY > 40);
        };
        shrinkCheck();
        window.addEventListener('scroll', shrinkCheck, { passive: true });
    }

    // Hide navbar on mobile when footer enters viewport
    (function() {
        var footer = document.querySelector('.site-footer') || document.querySelector('.dash-footer') || document.querySelector('.auth-footer');
        var navEl = document.querySelector('.navbar');
        if (!footer || !navEl) return;
        var observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (window.innerWidth <= 768) {
                    navEl.classList.toggle('navbar-hide', entry.isIntersecting);
                } else {
                    navEl.classList.remove('navbar-hide');
                }
            });
        }, { threshold: 0 });
        observer.observe(footer);
    })();

    document.querySelectorAll('.method-option').forEach(option => {
        option.addEventListener('click', () => {
            document.querySelectorAll('.method-option').forEach(item => item.classList.remove('active'));
            option.classList.add('active');
        });
    });

    document.querySelectorAll('[data-copy-target]').forEach(button => {
        button.addEventListener('click', async () => {
            const target = document.getElementById(button.dataset.copyTarget);
            if (!target) return;

            await navigator.clipboard?.writeText(target.value);
            const originalText = button.textContent;
            button.textContent = 'Copied';
            setTimeout(() => {
                button.textContent = originalText;
            }, 1200);
        });
    });

    document.getElementById('downloadReceiptBtn')?.addEventListener('click', () => {
        window.print();
    });
});
