# Business Impact Matrix
## Quick Reference for Decision Makers

**Last Updated**: January 2026  
**Reading Time**: 3 minutes

---

## 🎯 One-Page Risk Overview

This matrix translates 15 technical attack scenarios into **business consequences** and **financial impact**.

---

## 📊 COMPLETE IMPACT MATRIX

| Attack ID | Attack Type | What Happens If Successful | Financial Impact | Recovery Time | GDPR Risk |
|-----------|-------------|---------------------------|------------------|---------------|-----------|
| **DIR-001** | System Override | AI reveals customer purchase data | €20-50M | 12-24 months | ⚠️ Art. 32 violation |
| **DIR-002** | Instruction Negation | AI discloses supplier names & pricing | €10-30M | 6-12 months | ⚠️ Trade secret theft |
| **DIR-003** | Role Confusion | AI executes database queries | €30-60M | 18+ months | ⚠️ Critical violation |
| **DIR-004** | Emotional Manipulation | AI bypasses verification protocols | €5-15M | 3-6 months | ⚠️ Process failure |
| **DIR-005** | Gradual Trust Building | AI reveals system architecture | €5-10M | 6-12 months | ⚠️ Security by obscurity lost |
| **EXFIL-001** | Gradual Disclosure | UHNW customer data stolen incrementally | €25-75M | 24+ months | ⚠️ Systematic breach |
| **EXFIL-002** | Design IP Extraction | Unreleased collection leaked | €50-100M | 12-18 months | ❌ No GDPR but IP theft |
| **EXFIL-003** | Fake Customer | Order & shipping details exposed | €10-20M | 6-12 months | ⚠️ Personal data breach |
| **EXFIL-004** | Competitive Intel | Revenue & sales metrics leaked | €15-40M | 12-18 months | ❌ Business intelligence loss |
| **EXFIL-005** | Fake Partnership | Supplier contracts & pricing revealed | €20-50M | 12-24 months | ❌ Commercial confidence breach |
| **IND-001** | Poisoned Review | Hidden command exports customer emails | €30-80M | 18-24 months | ⚠️ Automated breach |
| **IND-002** | Obfuscated Text | White text attack extracts VIP list | €40-100M | 24+ months | ⚠️ Stealth exfiltration |
| **IND-003** | Multilingual | Chinese characters bypass filters | €20-60M | 12-18 months | ⚠️ Filter evasion |
| **IND-004** | Email Attachment | PDF metadata executes data queries | €25-70M | 12-24 months | ⚠️ Automated at scale |
| **IND-005** | Payload Splitting | Multi-part attack reassembles commands | €30-90M | 18+ months | ⚠️ Advanced persistent threat |

**TOTAL POTENTIAL EXPOSURE**: €335M - €855M (if all attacks succeed over 2 years)

**Legend**:
- ⚠️ GDPR violation (fines + lawsuits)
- ❌ No direct GDPR but severe business impact

---

## 💰 Cost Breakdown by Category

### Direct Injection Attacks
```
Total Financial Risk: €70M - €165M
Average Recovery: 11 months
GDPR Violations: 4 of 5 scenarios

Breakdown:
├─ Regulatory Fines:     €40M - €100M (20M per major breach)
├─ Legal Costs:          €10M - €25M (class actions, defense)
├─ Brand Damage:         €15M - €30M (customer churn, market cap)
└─ Remediation:          €5M - €10M (system overhaul, monitoring)
```

### Data Exfiltration Attacks
```
Total Financial Risk: €120M - €285M
Average Recovery: 13 months
GDPR Violations: 2 of 5 scenarios

Breakdown:
├─ IP Theft:             €50M - €100M (design collections)
├─ Customer Data:        €30M - €80M (UHNW privacy breach)
├─ Competitive Loss:     €25M - €70M (strategic intel leaked)
└─ Operational:          €15M - €35M (investigation, security upgrade)
```

### Indirect Injection Attacks
```
Total Financial Risk: €145M - €400M
Average Recovery: 17 months
GDPR Violations: 5 of 5 scenarios

Breakdown:
├─ Systematic Breach:    €60M - €150M (automated over time)
├─ Detection Delay:      €40M - €120M (stealth = longer exposure)
├─ Regulatory:           €30M - €90M (multiple violations)
└─ Reputation:           €15M - €40M (trust erosion)
```

---

## 🎯 Risk Prioritization for Budget Allocation

### Tier 1: CRITICAL (Immediate Investment Required)

| Attack | Why Critical | Budget Allocation |
|--------|-------------|-------------------|
| **IND-002** (Obfuscated Text) | €40-100M risk, hard to detect | €100K - Detection systems |
| **EXFIL-002** (Design IP) | €50-100M, core business asset | €80K - IP protection controls |
| **DIR-003** (Role Confusion) | €30-60M, direct DB access | €70K - Access control hardening |
| **IND-001** (Poisoned Review) | €30-80M, scalable attack | €90K - Content filtering |

**Tier 1 Total Investment**: €340K protects €150M - €340M exposure

---

### Tier 2: HIGH (Quarter 2 Priority)

| Attack | Why High Priority | Budget Allocation |
|--------|------------------|-------------------|
| **EXFIL-001** (Gradual Disclosure) | €25-75M, common social engineering | €50K - Conversation monitoring |
| **IND-004** (Email Attachment) | €25-70M, automated vector | €60K - Document sanitization |
| **DIR-001** (System Override) | €20-50M, easiest to attempt | €40K - Prompt hardening |

**Tier 2 Total Investment**: €150K protects €70M - €195M exposure

---

### Tier 3: MEDIUM (Quarter 3-4)

Remaining 8 scenarios: €190K investment protects €115M - €320M

**TOTAL DEFENSE BUDGET**: €680K protects €335M - €855M (ROI: 49,265% - 125,735%)

---

## 📈 Timeline & Milestones

### Month 1: Quick Wins (€100K)
- ✅ Implement input keyword blocking (DIR-001, DIR-002)
- ✅ Add output schema validation (EXFIL-003, EXFIL-004)
- ✅ Deploy basic HTML sanitization (IND-001)

**Risk Reduced**: €65M - €160M (19% of total exposure)

---

### Month 2-3: Core Defenses (€250K)
- ✅ Advanced content filtering (IND-002, IND-003)
- ✅ Human-in-the-loop for sensitive actions (DIR-003, EXFIL-002)
- ✅ Behavioral monitoring system (all categories)

**Risk Reduced**: €180M - €420M (54% of total exposure)

---

### Month 4-6: Complete Protection (€330K)
- ✅ AI security operations center
- ✅ Red team testing program
- ✅ Employee training & awareness
- ✅ Incident response automation

**Risk Reduced**: €335M - €855M (100% of identified exposure)

---

## 🏆 Success Metrics Dashboard

### Key Performance Indicators

| Metric | Baseline (No Defense) | Target (Month 6) | Measurement |
|--------|----------------------|------------------|-------------|
| **Successful Attacks** | 15 of 15 vulnerable | 0 of 15 | Weekly red team tests |
| **Detection Time** | N/A (no detection) | <15 minutes | SIEM alert latency |
| **False Positives** | N/A | <3% | Legitimate queries blocked |
| **Data Breach Incidents** | High risk | Zero | Security logs |
| **Customer Trust Score** | Baseline | +15% | NPS surveys |
| **Compliance Audit Score** | Unknown | 95%+ | GDPR/AI Act assessment |

---

## 💡 ROI Scenarios

### Conservative Scenario (25% Risk Reduction)
```
Investment:     €680K
Risk Mitigated: €84M (25% of €335M)
ROI:            12,253%
Payback:        3 days of prevented breach
```

### Realistic Scenario (75% Risk Reduction)
```
Investment:     €680K
Risk Mitigated: €464M (75% of €620M avg)
ROI:            68,135%
Payback:        1 day of prevented breach
```

### Best Case Scenario (100% Prevention)
```
Investment:     €680K
Risk Mitigated: €855M (worst-case prevented)
ROI:            125,635%
Payback:        <1 day of prevented breach
```

**In all scenarios, investment pays for itself in the first prevented incident.**

---

## 🎯 Decision Framework

### For C-Suite: 3 Questions

1. **Can we afford NOT to invest €680K?**
   - Single breach = €20-100M
   - Total exposure = €335-855M
   - Investment = 0.08-0.2% of exposure

2. **What's our risk appetite?**
   - Conservative: Do Tier 1 only (€340K)
   - Balanced: Do Tier 1-2 (€490K)
   - Comprehensive: Full program (€680K)

3. **When do we start?**
   - Immediate: High-risk defenses Month 1
   - Phased: Spread over 6 months
   - Delayed: Accept current exposure (NOT recommended)

---

## 📊 Competitor Benchmark

### Luxury AI Security Maturity

| Brand Tier | Current State | Investment Level | Breach Risk |
|-----------|---------------|------------------|-------------|
| **Laggards** | No AI security program | €0 | 90-100% vulnerable |
| **Followers** | Basic input filters | €50-150K | 60-80% vulnerable |
| **Standard** | Multi-layer defenses | €300-500K | 20-40% vulnerable |
| **Leaders** | This framework level | €600-800K | <10% vulnerable |
| **Innovators** | Continuous red team + AI monitoring | €1M+ | <5% vulnerable |

**Positioning Goal**: Move from current state → **Leader tier** (€680K investment)

**Competitive Advantage**: First luxury brand with NIST AI RMF certification

---

## 📄 Document Control

**Version**: 1.0  
**Status**: Portfolio Case Study  
**Confidentiality**: Public (No proprietary data)  
**Authority**: Based on OWASP, NIST, MITRE standards

**For Implementation Consultation**: Contact via GitHub portfolio

---

*"The question isn't whether we can afford to invest in AI security. The question is whether we can afford not to."*

**— Claudia Caroleo, AI Security Specialist**