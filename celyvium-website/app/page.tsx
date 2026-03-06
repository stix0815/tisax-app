'use client';

import Hero from "@/components/Hero";
import { motion, useScroll, useTransform } from 'framer-motion';
import { Bot, TrendingUp, BarChart, Sparkles, Zap, Brain } from 'lucide-react';
import Image from 'next/image';
import { useRef } from 'react';
import Link from 'next/link';

export default function Home() {
  const containerRef = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ["start start", "end end"]
  });

  const opacity1 = useTransform(scrollYProgress, [0, 0.2], [1, 0]);
  const scale1 = useTransform(scrollYProgress, [0, 0.2], [1, 0.8]);

  return (
    <main className="min-h-screen bg-deep-navy" ref={containerRef}>
      <Hero />
      
      {/* AI & Automation - Fullscreen Visual Section */}
      <section className="relative h-screen flex items-center overflow-hidden">
        <div className="absolute inset-0">
          <Image
            src="/images/ai-abstract.jpg"
            alt="AI Technology"
            fill
            className="object-cover opacity-40"
            priority
          />
          <div className="absolute inset-0 bg-gradient-to-r from-deep-navy via-deep-navy/80 to-transparent" />
        </div>

        <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <motion.div
            initial={{ opacity: 0, x: -50 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 1 }}
          >
            <div className="flex items-center gap-3 mb-6">
              <Brain className="text-neon-cyan" size={40} />
              <span className="text-neon-cyan font-semibold text-sm uppercase tracking-wider">
                Künstliche Intelligenz
              </span>
            </div>
            <h2 className="text-5xl lg:text-6xl font-bold mb-6 leading-tight">
              KI macht den
              <br />
              <span className="gradient-text">Unterschied.</span>
            </h2>
            <p className="text-xl text-cool-grey leading-relaxed mb-8">
              Automatisierung, die denkt. Workflows, die lernen. Content, der überzeugt.
              Wir setzen modernste KI-Technologie ein, um Ihre Prozesse zu revolutionieren.
            </p>
            <Link href="/services">
              <motion.button
                whileHover={{ scale: 1.05 }}
                className="px-8 py-4 bg-brand-gradient text-deep-navy font-semibold rounded-full"
              >
                Mehr erfahren
              </motion.button>
            </Link>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, x: 50 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 1, delay: 0.2 }}
            className="hidden lg:block"
          >
            <div className="relative">
              <div className="absolute inset-0 bg-brand-gradient opacity-20 blur-3xl rounded-full" />
              <div className="relative bg-navy/50 backdrop-blur-lg border border-electric-indigo/30 rounded-3xl p-8">
                <div className="space-y-4">
                  {[
                    { icon: <Sparkles size={24} />, text: 'Content-Generierung mit GPT-4' },
                    { icon: <Zap size={24} />, text: 'Automatisierte Workflows' },
                    { icon: <Bot size={24} />, text: 'Intelligente Chatbots' },
                  ].map((item, i) => (
                    <motion.div
                      key={i}
                      initial={{ opacity: 0, x: 20 }}
                      whileInView={{ opacity: 1, x: 0 }}
                      viewport={{ once: true }}
                      transition={{ delay: 0.4 + i * 0.1 }}
                      className="flex items-center gap-4 text-off-white"
                    >
                      <div className="text-neon-cyan">{item.icon}</div>
                      <span className="text-lg">{item.text}</span>
                    </motion.div>
                  ))}
                </div>
              </div>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Analytics - Split Screen */}
      <section className="relative min-h-screen flex items-center bg-gradient-to-b from-deep-navy to-navy py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true }}
            transition={{ duration: 0.8 }}
            className="order-2 lg:order-1"
          >
            <div className="relative rounded-3xl overflow-hidden border border-steel-blue shadow-2xl">
              <Image
                src="/images/analytics.jpg"
                alt="Data Analytics"
                width={800}
                height={600}
                className="w-full h-auto"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-deep-navy/80 to-transparent" />
            </div>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, x: 50 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 1 }}
            className="order-1 lg:order-2"
          >
            <div className="flex items-center gap-3 mb-6">
              <BarChart className="text-electric-indigo" size={40} />
              <span className="text-electric-indigo font-semibold text-sm uppercase tracking-wider">
                Datenbasiert
              </span>
            </div>
            <h2 className="text-5xl lg:text-6xl font-bold mb-6 leading-tight">
              Daten sprechen
              <br />
              <span className="gradient-text">lassen.</span>
            </h2>
            <p className="text-xl text-cool-grey leading-relaxed mb-8">
              Präzise Analyse. Klare Insights. Fundierte Entscheidungen.
              Wir verwandeln Ihre Daten in strategische Vorteile.
            </p>
            <div className="space-y-4">
              {['Real-time Dashboards', 'Custom Reports', 'Predictive Analytics'].map((item, i) => (
                <motion.div
                  key={i}
                  initial={{ opacity: 0, x: 20 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  viewport={{ once: true }}
                  transition={{ delay: 0.3 + i * 0.1 }}
                  className="flex items-center gap-3"
                >
                  <div className="w-2 h-2 rounded-full bg-brand-gradient" />
                  <span className="text-lg text-off-white">{item}</span>
                </motion.div>
              ))}
            </div>
          </motion.div>
        </div>
      </section>

      {/* Social Media - Fullscreen */}
      <section className="relative h-screen flex items-center overflow-hidden">
        <div className="absolute inset-0">
          <Image
            src="/images/social-media.jpg"
            alt="Social Media"
            fill
            className="object-cover opacity-30"
          />
          <div className="absolute inset-0 bg-gradient-to-l from-deep-navy via-deep-navy/80 to-transparent" />
        </div>

        <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-right ml-auto lg:w-1/2">
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 1 }}
          >
            <div className="flex items-center gap-3 mb-6 justify-end">
              <span className="text-vivid-purple font-semibold text-sm uppercase tracking-wider">
                Social Media
              </span>
              <TrendingUp className="text-vivid-purple" size={40} />
            </div>
            <h2 className="text-5xl lg:text-6xl font-bold mb-6 leading-tight">
              Communities
              <br />
              <span className="gradient-text">aufbauen.</span>
            </h2>
            <p className="text-xl text-cool-grey leading-relaxed mb-8">
              Von der Strategie bis zum Community-Management.
              Wir machen Ihre Marke in sozialen Netzwerken sichtbar und relevant.
            </p>
          </motion.div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="relative py-32 px-4 bg-navy overflow-hidden">
        {/* Background decoration */}
        <div className="absolute inset-0 pointer-events-none">
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-brand-gradient opacity-10 blur-[150px] rounded-full" />
        </div>

        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
          className="relative z-10 max-w-5xl mx-auto text-center"
        >
          <h2 className="text-5xl lg:text-7xl font-bold mb-8 leading-tight">
            Bereit für die{' '}
            <span className="gradient-text">Zukunft?</span>
          </h2>
          <p className="text-2xl text-cool-grey mb-12 max-w-3xl mx-auto leading-relaxed">
            Lassen Sie uns gemeinsam Ihre digitale Strategie auf das nächste Level bringen.
          </p>
          <Link href="/contact">
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              className="px-12 py-6 bg-brand-gradient text-deep-navy font-bold text-xl rounded-full hover:shadow-2xl hover:shadow-electric-indigo/50 transition-all duration-300"
            >
              Jetzt starten
            </motion.button>
          </Link>
        </motion.div>
      </section>
    </main>
  );
}
