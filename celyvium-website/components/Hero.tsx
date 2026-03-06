'use client';

import { motion } from 'framer-motion';
import { ArrowRight } from 'lucide-react';
import Link from 'next/link';

export default function Hero() {
  return (
    <section className="relative h-screen flex items-center justify-center overflow-hidden">
      {/* Animated Background Orb - subtler */}
      <div className="absolute inset-0 flex items-center justify-center pointer-events-none">
        <motion.div
          className="w-[800px] h-[800px] rounded-full opacity-20 blur-[100px]"
          style={{
            background: 'radial-gradient(circle at center, #68D7EF 0%, #6769DB 40%, #9E69DE 70%, transparent 100%)',
          }}
          animate={{
            scale: [1, 1.1, 1],
            opacity: [0.2, 0.25, 0.2],
          }}
          transition={{
            duration: 8,
            repeat: Infinity,
            ease: 'easeInOut',
          }}
        />
      </div>

      {/* Content */}
      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1, ease: 'easeOut' }}
        >
          {/* Main Headline - größer und impactvoller */}
          <h1 className="text-6xl sm:text-7xl lg:text-8xl xl:text-9xl font-bold mb-8 leading-[0.95] tracking-tight">
            Work,{' '}
            <span className="gradient-text">weightless.</span>
          </h1>

          {/* Subheadline */}
          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 1, delay: 0.3 }}
            className="text-lg sm:text-xl lg:text-2xl text-cool-grey mb-12 max-w-3xl mx-auto leading-relaxed"
          >
            Digitales Marketing neu gedacht. Mit KI, Automatisierung und datenbasierter Strategie bringen wir Ihre Marke in die Zukunft.
          </motion.p>

          {/* CTA Buttons */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 1, delay: 0.5 }}
            className="flex flex-col sm:flex-row gap-4 justify-center items-center"
          >
            <Link href="/services">
              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="px-10 py-5 bg-brand-gradient text-deep-navy font-semibold text-lg rounded-full hover:shadow-2xl hover:shadow-electric-indigo/50 transition-all duration-300 flex items-center gap-2"
              >
                Unsere Leistungen
                <ArrowRight size={22} />
              </motion.button>
            </Link>

            <Link href="/contact">
              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="px-10 py-5 border-2 border-electric-indigo/50 text-off-white font-semibold text-lg rounded-full hover:bg-electric-indigo/10 hover:border-electric-indigo transition-all duration-300"
              >
                Kontakt aufnehmen
              </motion.button>
            </Link>
          </motion.div>
        </motion.div>

        {/* Scroll Indicator */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 1, delay: 1 }}
          className="absolute bottom-16 left-1/2 transform -translate-x-1/2"
        >
          <motion.div
            animate={{ y: [0, 10, 0] }}
            transition={{ duration: 2, repeat: Infinity, ease: 'easeInOut' }}
            className="flex flex-col items-center gap-2"
          >
            <span className="text-xs text-cool-grey uppercase tracking-wider">Scroll</span>
            <div className="w-6 h-10 border-2 border-cool-grey/50 rounded-full flex justify-center pt-2">
              <motion.div
                animate={{ y: [0, 12, 0], opacity: [1, 0, 1] }}
                transition={{ duration: 2, repeat: Infinity, ease: 'easeInOut' }}
                className="w-1 h-3 bg-brand-gradient rounded-full"
              />
            </div>
          </motion.div>
        </motion.div>
      </div>
    </section>
  );
}
