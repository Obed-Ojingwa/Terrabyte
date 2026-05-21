import Link from "next/link";

export default function HomePage() {
  const stats = [
    { value: "2,400+", label: "Students Enrolled" },
    { value: "48", label: "Expert Courses" },
    { value: "96%", label: "Completion Rate" },
    { value: "100%", label: "Job-Ready Skills" },
  ];

  const heroCards = [
    { src: "/hero-card-1.svg", alt: "AI and data skills" },
    { src: "/hero-card-2.svg", alt: "Cloud computing preview" },
    { src: "/hero-card-3.svg", alt: "Design and product thinking" },
  ];

  const courses = [
    {
      title: "Cybersecurity Fundamentals",
      category: "Security",
      level: "Beginner",
      price: 75000,
      duration: "8 weeks",
      icon: "🔐",
      thumbnail: "/course-thumb-1.svg",
    },
    {
      title: "Data Analysis with Python",
      category: "Data Science",
      level: "Intermediate",
      price: 85000,
      duration: "10 weeks",
      icon: "📊",
      thumbnail: "/course-thumb-2.svg",
    },
    {
      title: "Cloud Architecture (AWS)",
      category: "Cloud",
      level: "Advanced",
      price: 120000,
      duration: "12 weeks",
      icon: "☁️",
      thumbnail: "/course-thumb-3.svg",
    },
    {
      title: "Full-Stack Web Development",
      category: "Development",
      level: "Intermediate",
      price: 95000,
      duration: "16 weeks",
      icon: "💻",
      thumbnail: "/course-thumb-1.svg",
    },
    {
      title: "UI/UX Design Mastery",
      category: "Design",
      level: "Beginner",
      price: 65000,
      duration: "8 weeks",
      icon: "🎨",
      thumbnail: "/course-thumb-2.svg",
    },
    {
      title: "Network Administration",
      category: "Networking",
      level: "Intermediate",
      price: 80000,
      duration: "10 weeks",
      icon: "🌐",
      thumbnail: "/course-thumb-3.svg",
    },
  ];

  const testimonials = [
    {
      name: "Amaka Johnson",
      title: "Cloud Engineer",
      quote: "Terrabyte Academy helped me switch careers in under four months. The hands-on projects were exactly what employers wanted.",
      rating: 5,
    },
    {
      name: "David Osei",
      title: "Security Analyst",
      quote: "The practical cybersecurity labs were the highlight. I landed a role with confidence after graduation.",
      rating: 5,
    },
    {
      name: "Rita Chukwu",
      title: "UI/UX Designer",
      quote: "The mentorship and real design challenges made a real difference in my portfolio.",
      rating: 5,
    },
  ];

  return (
    <div className="bg-[#03091A] text-white min-h-screen">
      <nav className="fixed top-0 left-0 right-0 z-50 flex flex-wrap items-center justify-between gap-4 px-6 md:px-12 py-4 border-b border-white/5 bg-[#03091A]/90 backdrop-blur-xl">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-gradient-to-br from-brand-500 to-brand-700 flex items-center justify-center font-black text-white">T</div>
          <span className="font-bold text-lg">Terrabyte <span className="text-brand-400">Academy</span></span>
        </div>
        <div className="hidden md:flex items-center gap-8 text-sm text-white/50">
          <Link href="#about" className="hover:text-white transition-colors">About</Link>
          <Link href="#courses" className="hover:text-white transition-colors">Courses</Link>
          <Link href="#testimonials" className="hover:text-white transition-colors">Testimonials</Link>
          <Link href="#contact" className="hover:text-white transition-colors">Contact</Link>
        </div>
        <div className="flex items-center gap-3">
          <Link href="/auth/login" className="text-sm text-white/60 hover:text-white px-4 py-2 transition-colors">Sign In</Link>
          <Link href="/auth/register" className="text-sm bg-brand-500 hover:bg-brand-600 px-5 py-2.5 rounded-xl font-semibold transition-all">Get Started</Link>
        </div>
      </nav>

      <main className="pt-24">
        <section className="relative min-h-[85vh] overflow-hidden">
          <div className="absolute top-0 left-1/2 h-full w-[1200px] -translate-x-1/2 rounded-full bg-brand-500/10 blur-[180px] pointer-events-none" />
          <div className="absolute inset-0 opacity-[0.03] bg-[radial-gradient(circle_at_top_left,_rgba(55,138,221,0.22),_transparent_35%)]" />
          <div className="relative max-w-7xl mx-auto px-6 md:px-12 py-24">
            <div className="max-w-4xl">
              <div className="inline-flex items-center gap-2 bg-brand-500/10 border border-brand-500/30 text-brand-400 text-xs font-semibold px-4 py-2 rounded-full mb-8 tracking-wide uppercase">
                <span className="w-1.5 h-1.5 rounded-full bg-brand-400 animate-pulse" /> Nigeria&apos;s Premier Tech Academy
              </div>
              <h1 className="text-5xl md:text-7xl font-black leading-[1.05] tracking-tight mb-6">Learn Skills That Actually Matter</h1>
              <p className="text-lg text-white/60 max-w-2xl leading-relaxed mb-10">Practical, project-based training for technology careers that pay. From cybersecurity and cloud to data science and product design, build real skills that employers recognise.</p>
              <div className="flex flex-col gap-4 sm:flex-row">
                <Link href="#courses" className="group inline-flex items-center gap-3 bg-brand-500 hover:bg-brand-600 px-8 py-4 rounded-2xl font-bold text-base transition-all shadow-lg shadow-brand-900/30">
                  Explore Courses <span className="group-hover:translate-x-1 transition-transform">→</span>
                </Link>
                <Link href="#contact" className="inline-flex items-center justify-center rounded-2xl border border-white/10 bg-white/5 px-8 py-4 text-base text-white/80 hover:text-white hover:bg-white/10 transition">Contact Us</Link>
              </div>
            </div>

            <div className="mt-20 grid gap-5 md:grid-cols-3">
              {heroCards.map((card, index) => (
                <div key={card.alt} className={`hero-card overflow-hidden rounded-[2rem] border border-white/10 bg-[#071428] shadow-2xl shadow-brand-900/10 ${index === 0 ? "animate-float-1" : index === 1 ? "animate-float-2" : "animate-float-3"}`}>
                  <img src={card.src} alt={card.alt} className="h-full w-full object-cover" />
                </div>
              ))}
            </div>
          </div>
        </section>

        <section id="about" className="py-24 px-6 md:px-12 max-w-7xl mx-auto">
          <div className="grid gap-12 lg:grid-cols-[1.2fr_0.8fr] items-center">
            <div>
              <p className="text-brand-400 text-sm font-semibold uppercase tracking-widest mb-3">About Us</p>
              <h2 className="text-4xl md:text-5xl font-black tracking-tight mb-6">We turn curious learners into confident tech professionals.</h2>
              <p className="text-white/60 leading-relaxed max-w-2xl mb-8">Terrabyte Academy combines expert-led instruction, live mentorship, and real projects to help students develop modern digital skills. Our programs are designed for people who want meaningful career growth, not just certificates.</p>
              <div className="grid gap-4 sm:grid-cols-3">
                <div className="rounded-3xl bg-white/5 border border-white/10 p-6">
                  <p className="text-3xl font-black text-white">300+</p>
                  <p className="mt-2 text-sm text-white/50">Projects completed</p>
                </div>
                <div className="rounded-3xl bg-white/5 border border-white/10 p-6">
                  <p className="text-3xl font-black text-white">24/7</p>
                  <p className="mt-2 text-sm text-white/50">Mentor support</p>
                </div>
                <div className="rounded-3xl bg-white/5 border border-white/10 p-6">
                  <p className="text-3xl font-black text-white">98%</p>
                  <p className="mt-2 text-sm text-white/50">Student satisfaction</p>
                </div>
              </div>
            </div>
            <div className="rounded-[2.5rem] border border-white/10 bg-[#06102A] p-8 shadow-2xl shadow-brand-900/20">
              <div className="text-sm text-brand-400 uppercase tracking-[0.3em] mb-4">Company overview</div>
              <p className="text-white/70 leading-relaxed mb-6">We build learning experiences that focus on career outcomes. Each course is shaped around employer expectations, real tools, and portfolio-ready work to help learners create momentum from day one.</p>
              <div className="space-y-4 text-white/70">
                <div className="flex items-start gap-3">
                  <span className="mt-1 text-brand-400">•</span>
                  <span>Hands-on labs with real-world tools.</span>
                </div>
                <div className="flex items-start gap-3">
                  <span className="mt-1 text-brand-400">•</span>
                  <span>Supportive mentorship from working professionals.</span>
                </div>
                <div className="flex items-start gap-3">
                  <span className="mt-1 text-brand-400">•</span>
                  <span>Flexible online delivery with track options.</span>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section id="courses" className="py-24 px-6 md:px-12 max-w-7xl mx-auto">
          <div className="flex flex-col gap-8 md:flex-row md:items-end md:justify-between mb-12">
            <div>
              <p className="text-brand-400 text-sm font-semibold uppercase tracking-widest mb-3">What We Offer</p>
              <h2 className="text-4xl md:text-5xl font-black tracking-tight">Featured Courses with Thumbnails</h2>
            </div>
            <Link href="/public/courses" className="inline-flex items-center gap-2 text-sm text-white/40 hover:text-white transition-colors">View all courses →</Link>
          </div>
          <div className="grid grid-cols-1 gap-6 md:grid-cols-2 xl:grid-cols-3">
            {courses.map((course) => (
              <Link href="/public/courses" key={course.title} className="group overflow-hidden rounded-[2rem] border border-white/10 bg-[#071428] transition hover:-translate-y-1 hover:border-brand-500/40 shadow-xl shadow-brand-900/10">
                <div className="relative h-56 overflow-hidden bg-[#0a1323]">
                  <img src={course.thumbnail} alt={course.title} className="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105" />
                  <div className="absolute inset-x-0 bottom-0 h-24 bg-gradient-to-t from-[#03091A] to-transparent" />
                  <div className="absolute left-5 bottom-5 text-sm text-white/80 uppercase tracking-[0.28em]">{course.category}</div>
                </div>
                <div className="p-6">
                  <div className="flex items-center justify-between mb-3">
                    <span className="rounded-full bg-white/5 px-3 py-1 text-[11px] uppercase tracking-[0.28em] text-white/50">{course.level}</span>
                    <span className="text-3xl">{course.icon}</span>
                  </div>
                  <h3 className="text-xl font-bold text-white mb-3">{course.title}</h3>
                  <p className="text-sm text-white/50 mb-6">{course.duration} • Certificate included • Hands-on labs</p>
                  <div className="flex items-center justify-between gap-4 text-sm text-white/40">
                    <span>From ₦{course.price.toLocaleString()}</span>
                    <span className="text-brand-400 font-semibold">Enroll →</span>
                  </div>
                </div>
              </Link>
            ))}
          </div>
        </section>

        <section id="testimonials" className="py-24 px-6 md:px-12 max-w-7xl mx-auto">
          <div className="mb-14 text-center">
            <p className="text-brand-400 text-sm font-semibold uppercase tracking-widest mb-3">Student Success</p>
            <h2 className="text-4xl md:text-5xl font-black tracking-tight">Real stories from graduates</h2>
          </div>
          <div className="grid gap-6 xl:grid-cols-3">
            {testimonials.map((item) => (
              <div key={item.name} className="rounded-[2rem] border border-white/10 bg-[#071428]/90 p-8 shadow-xl shadow-brand-900/20">
                <div className="flex items-center gap-4 mb-6">
                  <div className="flex h-14 w-14 items-center justify-center rounded-3xl bg-brand-500/10 text-brand-300 text-xl">{item.name.split(" ").map((part) => part[0]).join("")}</div>
                  <div>
                    <p className="font-bold text-white">{item.name}</p>
                    <p className="text-sm text-white/50">{item.title}</p>
                  </div>
                </div>
                <p className="text-white/70 leading-relaxed mb-6">“{item.quote}”</p>
                <div className="flex items-center gap-2 text-brand-400 text-sm font-semibold">
                  {Array.from({ length: item.rating }).map((_, index) => (
                    <span key={index}>★</span>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </section>

        <section id="contact" className="pb-24 px-6 md:px-12 max-w-7xl mx-auto">
          <div className="grid gap-10 lg:grid-cols-[1.2fr_0.8fr] items-center">
            <div>
              <p className="text-brand-400 text-sm font-semibold uppercase tracking-widest mb-3">Get in touch</p>
              <h2 className="text-4xl md:text-5xl font-black tracking-tight mb-6">Ready to start your tech journey?</h2>
              <p className="text-white/60 leading-relaxed max-w-2xl mb-8">Contact our admissions team, request a course brochure, or book a free discovery call. We’re here to help you choose the path that fits your goals.</p>
              <div className="grid gap-4 sm:grid-cols-2">
                <div className="rounded-3xl bg-white/5 border border-white/10 p-6">
                  <p className="text-sm text-white/50">WhatsApp</p>
                  <p className="mt-2 font-semibold text-white">+234 812 345 6789</p>
                </div>
                <div className="rounded-3xl bg-white/5 border border-white/10 p-6">
                  <p className="text-sm text-white/50">Email</p>
                  <p className="mt-2 font-semibold text-white">hello@terrabyte.academy</p>
                </div>
              </div>
            </div>
            <div className="rounded-[2.5rem] border border-white/10 bg-[#06102A] p-8 shadow-2xl shadow-brand-900/20">
              <p className="text-sm uppercase tracking-[0.3em] text-brand-400 mb-4">Quick contact</p>
              <div className="space-y-4">
                <div className="rounded-3xl bg-white/5 p-5">
                  <p className="text-white/60 text-sm">Send a message</p>
                  <p className="mt-3 font-semibold text-white">Fill the online form and we&apos;ll reply in 24 hours.</p>
                </div>
                <div className="rounded-3xl bg-white/5 p-5">
                  <p className="text-white/60 text-sm">Call admissions</p>
                  <p className="mt-3 font-semibold text-white">+234 812 345 6789</p>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>

      <footer className="border-t border-white/5 px-6 md:px-12 py-16 bg-[#020712]">
        <div className="max-w-7xl mx-auto grid gap-12 lg:grid-cols-4">
          <div className="space-y-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-2xl bg-gradient-to-br from-brand-500 to-brand-700 flex items-center justify-center font-black text-white">T</div>
              <div>
                <p className="font-bold text-white">Terrabyte Academy</p>
                <p className="text-sm text-white/50">Building tech careers across Africa.</p>
              </div>
            </div>
            <div className="text-sm text-white/50">
              <p>+234 812 345 6789</p>
              <p>hello@terrabyte.academy</p>
            </div>
          </div>
          <div>
            <p className="text-sm uppercase tracking-[0.3em] text-brand-400 mb-4">Company</p>
            <div className="space-y-3 text-sm text-white/50">
              <Link href="#about" className="block hover:text-white">About Us</Link>
              <Link href="#contact" className="block hover:text-white">Contact Us</Link>
              <Link href="/public/courses" className="block hover:text-white">Courses</Link>
              <Link href="/public/blog" className="block hover:text-white">Blog</Link>
            </div>
          </div>
          <div>
            <p className="text-sm uppercase tracking-[0.3em] text-brand-400 mb-4">Resources</p>
            <div className="space-y-3 text-sm text-white/50">
              <Link href="/public/events" className="block hover:text-white">Events</Link>
              <Link href="/public/verify-certificate" className="block hover:text-white">Verify Certificate</Link>
              <Link href="#testimonials" className="block hover:text-white">Testimonials</Link>
              <Link href="#" className="block hover:text-white">Support</Link>
            </div>
          </div>
          <div>
            <p className="text-sm uppercase tracking-[0.3em] text-brand-400 mb-4">Social</p>
            <div className="flex flex-wrap gap-3">
              <a href="https://wa.me/2348123456789" className="rounded-3xl bg-white/5 px-4 py-3 text-sm text-white/80 hover:bg-brand-500/10 transition">WhatsApp</a>
              <Link href="#contact" className="rounded-3xl bg-white/5 px-4 py-3 text-sm text-white/80 hover:bg-brand-500/10 transition">Contact</Link>
            </div>
          </div>
        </div>
        <div className="mt-12 border-t border-white/10 pt-8 text-center text-xs text-white/30">© {new Date().getFullYear()} Terrabyte Academy. All rights reserved.</div>
      </footer>
    </div>
  );
}
