import Link from "next/link";

export default function NotFound() {
  return (
    <main className="min-h-screen bg-[#03091A] text-white flex items-center justify-center px-6 py-24">
      <div className="max-w-2xl rounded-[2rem] border border-white/10 bg-[#071428]/95 p-12 text-center shadow-2xl shadow-brand-900/20">
        <p className="text-sm uppercase tracking-[0.3em] text-brand-400 mb-4">Page not found</p>
        <h1 className="text-5xl font-black mb-6">404</h1>
        <p className="text-white/70 mb-8">The page you&apos;re looking for does not exist or may have been moved.</p>
        <Link href="/" className="inline-flex items-center justify-center rounded-2xl bg-brand-500 px-8 py-4 text-sm font-semibold text-white hover:bg-brand-600 transition">Back to homepage</Link>
      </div>
    </main>
  );
}
