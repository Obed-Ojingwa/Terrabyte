import Link from "next/link";

export default function NotFound() {
  return (
    <main className="min-h-screen bg-[var(--primary)]/90 text-[var(--text)] flex items-center justify-center px-6 py-24">
      <div className="max-w-2xl rounded-[2rem] border border-[var(--muted)]/20 bg-[var(--surface)]/90 p-12 text-center shadow-2xl shadow-[var(--primary)]/20">
        <p className="text-sm uppercase tracking-[0.3em] text-[var(--primary)] mb-4">Page not found</p>
        <h1 className="text-5xl font-[var(--text)] mb-6">404</h1>
        <p className="text-[var(--text)]/70 mb-8">The page you&apos;re looking for does not exist or may have been moved.</p>
        <Link href="/" className="inline-flex items-center justify-center rounded-2xl bg-[var(--primary)] px-8 py-4 text-sm font-semibold text-[var(--text)] hover:bg-[var(--primary)-600 transition">Back to homepage</Link>
      </div>
    </main>
  );
}
