'use client';

import { motion } from 'framer-motion';
import Image from 'next/image';
import { Target, Lightbulb, Rocket } from 'lucide-react';

export default function About() {
  return (
    <main className="min-h-screen bg-deep-navy">
      {/* Hero Section with Image */}
      <section className="relative h-[60vh] flex items-center overflow-hidden">
        <div className="absolute inset-0">
          <Image
            src="/images/team.jpg"
            alt="Team"
            fill
            className="object-cover opacity-30"
          />
          <div className="absolute inset-0 bg-gradient-to-b from-deep-navy/60 to-deep-navy" />
        </div>

        <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <motion.h1
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="text-6xl lg:text-7xl font-bold mb-6"
          >
            Über <span className="gradient-text">Celyvium</span>
          </motion.h1>
          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.8, delay: 0.3 }}
            className="text-2xl text-cool-grey max-w-3xl mx-auto"
          >
            Work, weightless.
          </motion.p>
        </div>
      </section>

      {/* Story Section */}
      <section className="py-20 px-4">
        <div className="max-w-4xl mx-auto">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.8 }}
            className="space-y-8 text-lg leading-relaxed"
          >
            <p className="text-cool-grey">
              Celyvium steht für digitales Marketing, das keine Kompromisse eingeht. 
              Wir verbinden kreative Exzellenz mit technologischer Innovation, 
              um Marken in der digitalen Welt erfolgreich zu machen.
            </p>

            <p className="text-cool-grey">
              Unser Fokus liegt auf{' '}
              <span className="text-neon-cyan font-semibold">KI-gestützter Automatisierung</span>,{' '}
              <span className="text-electric-indigo font-semibold">datenbasierter Strategie</span> und{' '}
              <span className="text-vivid-purple font-semibold">erstklassigem Content</span>.
            </p>
          </motion.div>
        </div>
      </section>

      {/* Values Grid */}
      <section className="py-20 px-4 bg-gradient-to-b from-deep-navy to-navy">
        <div className="max-w-7xl mx-auto">
          <motion.h2
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            viewport={{ once: true }}
            className="text-5xl font-bold text-center mb-16"
          >
            <span className="gradient-text">Unsere Werte</span>
          </motion.h2>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {[
              {
                icon: <Rocket size={48} />,
                title: 'Innovation',
                description: 'Wir setzen auf modernste Technologien und denken voraus, nicht hinterher.',
              },
              {
                icon: <Target size={48} />,
                title: 'Präzision',
                description: 'Datenbasierte Entscheidungen statt Bauchgefühl. Jede Kampagne ist messbar.',
              },
              {
                icon: <Lightbulb size={48} />,
                title: 'Kreativität',
                description: 'Technologie ist unser Werkzeug. Kreativität ist unsere Superkraft.',
              },
            ].map((value, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.6, delay: index * 0.2 }}
                className="bg-navy/30 backdrop-blur-lg border border-steel-blue rounded-3xl p-10 hover:border-electric-indigo transition-all duration-500 text-center"
              >
                <div className="text-neon-cyan mb-6 flex justify-center">
                  {value.icon}
                </div>
                <h3 className="text-2xl font-bold mb-4 gradient-text">
                  {value.title}
                </h3>
                <p className="text-cool-grey leading-relaxed">
                  {value.description}
                </p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Mission Section */}
      <section className="py-32 px-4">
        <div className="max-w-5xl mx-auto text-center">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.8 }}
          >
            <h2 className="text-5xl lg:text-6xl font-bold mb-8">
              Unsere <span className="gradient-text">Mission</span>
            </h2>
            <p className="text-2xl text-cool-grey leading-relaxed">
              Wir machen digitales Marketing{' '}
              <span className="font-bold text-off-white">weightless</span> – 
              leicht, effizient und wirkungsvoll. Durch den intelligenten Einsatz 
              von KI und Automatisierung schaffen wir Raum für das, was wirklich zählt: 
              kreative Strategien und echte Ergebnisse.
            </p>
          </motion.div>
        </div>
      </section>
    </main>
  );
}
