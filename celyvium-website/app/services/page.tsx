'use client';

import { motion } from 'framer-motion';
import { Bot, TrendingUp, Zap, BarChart, Megaphone, Code } from 'lucide-react';

export default function Services() {
  const services = [
    {
      icon: <Bot size={40} />,
      title: 'KI & Automatisierung',
      description:
        'Intelligente Prozessautomatisierung, die Ihr Team entlastet und gleichzeitig Qualität und Geschwindigkeit erhöht.',
      features: [
        'Content-Automatisierung mit KI',
        'Workflow-Optimierung',
        'Chatbots & Assistenten',
      ],
    },
    {
      icon: <Megaphone size={40} />,
      title: 'Social Media Management',
      description:
        'Strategische Planung, kreative Umsetzung und Community-Management auf allen relevanten Plattformen.',
      features: [
        'Content-Strategie & Planung',
        'Community Management',
        'Influencer Marketing',
      ],
    },
    {
      icon: <BarChart size={40} />,
      title: 'Datenbasierte Analyse',
      description:
        'Fundierte Insights durch präzise Datenanalyse, Reporting und strategische Empfehlungen.',
      features: [
        'Performance Tracking',
        'Custom Dashboards',
        'Strategic Reporting',
      ],
    },
    {
      icon: <Code size={40} />,
      title: 'SaaS & Webentwicklung',
      description:
        'Entwicklung und Betrieb webbasierter Anwendungen, die Ihre Prozesse digitalisieren.',
      features: [
        'Custom Web-Apps',
        'SaaS-Plattformen',
        'API-Integrationen',
      ],
    },
    {
      icon: <TrendingUp size={40} />,
      title: 'Beratung & Strategie',
      description:
        'Ganzheitliche Beratung für Ihre digitale Transformation und langfristige Erfolgsstrategien.',
      features: [
        'Digital Strategy',
        'Workshops & Trainings',
        'Tech Consulting',
      ],
    },
    {
      icon: <Zap size={40} />,
      title: 'Content-Erstellung',
      description:
        'Hochwertige digitale Inhalte, die Ihre Marke zum Leben erwecken und Ihre Zielgruppe begeistern.',
      features: [
        'Video & Motion Graphics',
        'Copywriting',
        'Design & Branding',
      ],
    },
  ];

  return (
    <main className="min-h-screen bg-deep-navy pt-32 pb-20 px-4">
      <div className="max-w-7xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="text-center mb-16"
        >
          <h1 className="text-5xl font-bold mb-6">
            Unsere <span className="gradient-text">Leistungen</span>
          </h1>
          <p className="text-xl text-cool-grey max-w-3xl mx-auto">
            Maßgeschneiderte Lösungen für Ihr digitales Marketing – von Strategie bis Umsetzung.
          </p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {services.map((service, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              className="bg-navy/50 backdrop-blur-lg border border-steel-blue rounded-2xl p-8 hover:border-electric-indigo hover:scale-105 transition-all duration-300"
            >
              <div className="text-neon-cyan mb-4">{service.icon}</div>
              <h3 className="text-2xl font-semibold mb-4 gradient-text">
                {service.title}
              </h3>
              <p className="text-cool-grey mb-6 leading-relaxed">
                {service.description}
              </p>
              <ul className="space-y-2">
                {service.features.map((feature, idx) => (
                  <li key={idx} className="text-off-white flex items-center gap-2">
                    <span className="w-1.5 h-1.5 rounded-full bg-brand-gradient"></span>
                    {feature}
                  </li>
                ))}
              </ul>
            </motion.div>
          ))}
        </div>
      </div>
    </main>
  );
}
