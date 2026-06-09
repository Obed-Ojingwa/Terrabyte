"use client";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";
import Link from "next/link";
import { useLogin } from "@/hooks/useAuth";
import { useState } from "react";

const schema = z.object({ email: z.string().email("Enter a valid email"), password: z.string().min(6, "At least 6 characters") });
type FormData = z.infer<typeof schema>;
const inputClsLight = "w-full bg-[var(--surface)]/20 border border-[var(--muted)]/10 focus:border-[var(--primary)] text-[var(--text)] placeholder:text-[var(--text)]/20 rounded-xl px-4 py-3.5 text-sm outline-none transition-all focus:ring-1 focus:ring-[var(--primary)]/40";

export default function LoginPage() {
  const { mutate: login, isPending } = useLogin();
  const [showPw, setShowPw] = useState(false);
  const { register, handleSubmit, formState: { errors } } = useForm<FormData>({ resolver: zodResolver(schema) });
  return (
    <div className="min-h-screen flex overflow-hidden bg-[var(--primary)-900]">
      <div className="hidden lg:flex lg:w-1/2 relative flex-col justify-between p-14 overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-[var(--primary)]/20 via-[var(--primary)]/10 to-[var(--surface)]" />
        <div className="absolute inset-0 opacity-[0.02]" style={{ backgroundImage: "linear-gradient(var(--primary) 1px,transparent 1px),linear-gradient(90deg,var(--primary) 1px,transparent 1px)", backgroundSize: "48px 48px" }} />
        <div className="relative flex items-center gap-3 z-10">
          <div className="w-10 h-10 rounded-xl bg-[var(--surface)]/10 border border-[var(--muted)]/20 flex items-center justify-center font-black text-[var(--text)]">T</div>
          <span className="font-bold text-[var(--text)] text-lg">Terrabyte <span className="text-[var(--primary)]">Academy</span></span>
        </div>
        <div className="relative z-10">
          <div className="text-6xl text-[var(--primary)]/30 font-serif leading-none mb-3">&ldquo;</div>
          <p className="text-[var(--text)]/60 text-xl font-medium leading-relaxed max-w-sm mb-6">The investment I made at Terrabyte paid back tenfold within six months of graduating.</p>
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-full bg-[var(--primary)]/20 flex items-center justify-center text-xs font-bold text-[var(--text)]">EN</div>
            <div><p className="font-semibold text-[var(--text)]">Emeka Nwosu</p><p className="text-[var(--text)]/40 text-xs">Data Engineer, Flutterwave</p></div>
          </div>
        </div>
        <div className="relative z-10 grid grid-cols-3 gap-4">
          {[{n:"2,400+",l:"Students"},{n:"48",l:"Courses"},{n:"96%",l:"Completion"}].map(s=>(
            <div key={s.l} className="bg-[var(--surface)]/5 border border-[var(--muted)]/10 rounded-xl p-4"><p className="text-[var(--text)] font-black text-xl">{s.n}</p><p className="text-[var(--text)]/40 text-xs mt-0.5">{s.l}</p></div>
          ))}
        </div>
      </div>
      <div className="flex-1 flex items-center justify-center px-6 py-16 bg-[var(--bg)]">
        <div className="w-full max-w-md">
          <div className="flex items-center gap-3 mb-10 lg:hidden">
            <div className="w-9 h-9 rounded-xl bg-[var(--primary)] flex items-center justify-center font-black text-sm text-[var(--text)]">T</div>
            <span className="font-bold text-[var(--text)] text-lg">Terrabyte Academy</span>
          </div>
          <h1 className="text-3xl font-black text-[var(--text)] mb-1 tracking-tight">Welcome back</h1>
          <p className="text-[var(--text)]/40 text-sm mb-10">Sign in to continue your learning journey</p>
          <form onSubmit={handleSubmit((d) => login(d))} className="space-y-5">
            <div>
              <label className="block text-xs font-semibold text-[var(--text)]/40 uppercase tracking-widest mb-2">Email Address</label>
              <input {...register("email")} type="email" placeholder="you@example.com" className={inputClsLight} />
              {errors.email && <p className="text-[var(--primary)] text-xs mt-1.5">⚠ {errors.email.message}</p>}
            </div>
            <div>
              <div className="flex justify-between items-center mb-2"><label className="text-xs font-semibold text-[var(--text)]/40 uppercase tracking-widest">Password</label><Link href="/auth/forgot-password" className="text-xs text-[var(--primary)] hover:text-[var(--primary)-600">Forgot password?</Link></div>
              <div className="relative">
                <input {...register("password")} type={showPw ? "text" : "password"} placeholder="••••••••" className={inputClsLight + " pr-11"} />
                <button type="button" onClick={() => setShowPw(!showPw)} className="absolute right-3 top-1/2 -translate-y-1/2 text-[var(--text)]/30 hover:text-[var(--text)]/40 transition-colors text-sm">{showPw ? "🙈" : "👁"}</button>
              </div>
              {errors.password && <p className="text-[var(--primary)] text-xs mt-1.5">⚠ {errors.password.message}</p>}
            </div>
            <button type="submit" disabled={isPending} className="w-full bg-[var(--primary)] hover:bg-[var(--primary)-600 disabled:opacity-50 text-[var(--text)] font-bold py-3.5 rounded-xl transition-all flex items-center justify-center gap-2 shadow-lg shadow-[var(--primary)]/20 mt-2">
              {isPending ? <span className="w-5 h-5 border-2 border-[var(--muted)]/30 border-t-[var(--muted)]/20 rounded-full animate-spin" /> : <>Sign In →</>}
            </button>
          </form>
          <div className="relative my-8"><div className="absolute inset-0 flex items-center"><div className="w-full border-t border-[var(--muted)]/5" /></div><div className="relative flex justify-center"><span className="bg-[var(--primary)]/90 px-3 text-xs text-[var(--text)]/20">New to Terrabyte?</span></div></div>
          <Link href="/auth/register" className="w-full block text-center border border-[var(--muted)]/10 hover:border-[var(--muted)]/20 text-[var(--text)]/60 hover:text-[var(--text)] font-semibold py-3.5 rounded-xl transition-all text-sm bg-[var(--primary)]/90">Create an Account</Link>
        </div>
      </div>
    </div>
  );
}
