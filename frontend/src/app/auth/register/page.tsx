"use client";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";
import Link from "next/link";
import { useRegister } from "@/hooks/useAuth";

const schema = z.object({
  first_name: z.string().min(1,"Required"),
  middle_name: z.string().optional(),
  last_name: z.string().min(1,"Required"),
  email: z.string().email("Valid email required"),
  phone: z.string().min(1,"Required"),
  password: z.string().min(8,"At least 8 characters"),
  confirm_password: z.string()
}).refine(d=>d.password===d.confirm_password,{message:"Passwords don't match",path:["confirm_password"]});
type FormData = z.infer<typeof schema>;
const inputCls = "w-full bg-[var(--surface)]/20 border border-[var(--muted)]/20 focus:border-brand-500 text-[var(--text)] placeholder:text-[var(--text)]/20 rounded-xl px-4 py-3 text-sm outline-none transition-all focus:ring-1 focus:ring-brand-500/40";

export default function RegisterPage() {
  const { mutate: reg, isPending } = useRegister();
  const { register, handleSubmit, formState: { errors } } = useForm<FormData>({ resolver: zodResolver(schema) });
  return (
    <div className="min-h-screen flex items-center justify-center px-6 py-16 bg-[var(--bg)]">
      <div className="absolute inset-0 opacity-[0.03]" style={{ backgroundImage: "linear-gradient(#378add 1px,transparent 1px),linear-gradient(90deg,#378add 1px,transparent 1px)", backgroundSize: "60px 60px" }} />
      <div className="relative w-full max-w-lg">
        <div className="text-center mb-8">
          <Link href="/" className="inline-flex items-center gap-3 mb-8">
            <div className="w-10 h-10 rounded-xl bg-brand-600 flex items-center justify-center font-black text-base text-white">T</div>
            <span className="font-bold text-[var(--text)] text-lg">Terrabyte <span className="text-brand-300">Academy</span></span>
          </Link>
          <h1 className="text-3xl font-black text-[var(--text)] tracking-tight">Create your account</h1>
          <p className="text-[var(--text)]/40 text-sm mt-2">Join 2,400+ students already learning</p>
        </div>
        <div className="bg-[var(--surface)]/20 border border-[var(--muted)]/20 rounded-3xl p-8">
          <form onSubmit={handleSubmit((d) => reg(d))} className="space-y-4">
            <div className="grid grid-cols-2 gap-4">
              <div><label className="block text-xs font-semibold text-[var(--text)]/40 uppercase tracking-widest mb-2">First Name</label><input {...register("first_name")} placeholder="Adaeze" className={inputCls} />{errors.first_name && <p className="text-red-400 text-xs mt-1">⚠ {errors.first_name.message}</p>}</div>
              <div><label className="block text-xs font-semibold text-[var(--text)]/40 uppercase tracking-widest mb-2">Middle Name (Optional)</label><input {...register("middle_name")} placeholder="Chukwuma" className={inputCls} />{errors.middle_name && <p className="text-red-400 text-xs mt-1">⚠ {errors.middle_name.message}</p>}</div>
            </div>
            <div><label className="block text-xs font-semibold text-[var(--text)]/40 uppercase tracking-widest mb-2">Last Name</label><input {...register("last_name")} placeholder="Okonkwo" className={inputCls} />{errors.last_name && <p className="text-red-400 text-xs mt-1">⚠ {errors.last_name.message}</p>}</div>
            <div><label className="block text-xs font-semibold text-[var(--text)]/40 uppercase tracking-widest mb-2">Email</label><input {...register("email")} type="email" placeholder="you@example.com" className={inputCls} />{errors.email && <p className="text-red-400 text-xs mt-1">⚠ {errors.email.message}</p>}</div>
            <div><label className="block text-xs font-semibold text-[var(--text)]/40 uppercase tracking-widest mb-2">Phone Number</label><input {...register("phone")} placeholder="+234 800 000 0000" className={inputCls} />{errors.phone && <p className="text-red-400 text-xs mt-1">⚠ {errors.phone.message}</p>}</div>
            <div><label className="block text-xs font-semibold text-[var(--text)]/40 uppercase tracking-widest mb-2">Password</label><input {...register("password")} type="password" placeholder="Min. 8 characters" className={inputCls} />{errors.password && <p className="text-red-400 text-xs mt-1">⚠ {errors.password.message}</p>}</div>
            <div><label className="block text-xs font-semibold text-[var(--text)]/40 uppercase tracking-widest mb-2">Confirm Password</label><input {...register("confirm_password")} type="password" placeholder="Repeat password" className={inputCls} />{errors.confirm_password && <p className="text-red-400 text-xs mt-1">⚠ {errors.confirm_password.message}</p>}</div>
            <button type="submit" disabled={isPending} className="w-full bg-brand-500 hover:bg-brand-600 disabled:opacity-50 text-white font-bold py-3.5 rounded-xl transition-all flex items-center justify-center mt-2 shadow-lg shadow-brand-900/40">
              {isPending ? <span className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" /> : "Create Account"}
            </button>
          </form>
          <p className="text-center text-xs text-[var(--text)]/25 mt-5">By registering you agree to our <Link href="#" className="text-brand-400 hover:underline">Terms of Service</Link></p>
        </div>
        <p className="text-center text-sm text-[var(--text)]/35 mt-6">Already have an account? <Link href="/auth/login" className="text-brand-400 font-semibold hover:text-brand-300 transition-colors">Sign in</Link></p>
      </div>
    </div>
  );
}